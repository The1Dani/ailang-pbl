grammar AiLang;

// --- Parser Rules ---

prog: stat+;

block:
	ARR label? context	# Block2Block
	| label ARR label? context	# Label2Block;

label: '@' id;

context: '{' stat* '}';

// Changed: referenced the Lexer token BOOL_OP correctly
bool_context: '{' bool_group* '}';

bool_group: bool_stat (BOOL_OP bool_stat)*;

bool_stat: expr BOOL_OP expr;

assignment: assignable ':=' expr;

// Added back the 'id' rule since some of your other rules reference it
id: ID;

ref_op: assignable REF expr;

// column_ref_op: column REF expr;

stat:
	func_def		# functionDef 
	| assignment	# assign //ok
	| ref_op		# reference //ok
	| expr			# printExpr //ok
	| block			# block_stat //ok
	| doIfElse		# do_if_else //ok
	| fromToData	# load_op; //dummy implemented

// Fixed: Corrected the parameter list and ID references
func_def: FUNCTION id REF '(' id (',' id)* ')' context;

fromToData: FROM str ARR id;

doIfElse: DO context IF bool_context (ELSE context)?;


expr:
	basic_val			# basicValExpr
	| assignable         # pathExpr
	| func				# function
	| list				# listValExpr
	| df				# dataframe
	| '(' expr ')'		# group
    | expr REF arg_list  # methodCall     // Handles the <- (...) trigger
    | expr MATH_OP expr  # mathOp
    ;

assignable:
    id                        # simpleTarget
    | assignable '.' member   # memberTarget  // Allows x.y, df.col, df.1.sub
    ;

named_arg: id '=' expr;

arg: named_arg | expr;

arg_list: '(' (arg (',' arg)*)? ')';

generic_list: '(' expr (',' expr)* ')';

list: basic_list | generic_list | id;

df: '[' df_val (',' df_val)* ']';

df_val: (id ':')? basic_list;


member: 
    id    #basicIDMember
    | INT #intIDMember
    | '@' id #listIDMember             // Keeps your label/set logic
    ;

// column_method: column '.' id (REF arg_list)?;

func: '.' id (REF arg_list)?;

basic_list:
	'(' num (',' num)* ')'		# numList
	| '(' str (',' str)* ')'	# strList;

basic_val:
	//Consider bool
	num					# number
	| str				# string
	| '(' basic_val ')'	# group_basic_val;

num: INT # intigerLiteral | FLOAT # floatLiteral;

str: STR;

// --- Lexer Rules ---

DO: 'do';
IF: 'if';
ELSE: 'else';
FROM: 'from';
FUNCTION: 'function';

ARR: '->';
REF: '<-';

MATH_OP: '+' | '-' | '*' | '/';
BOOL_OP: '>' | '<' | '==' | '&' | '|';

STR: '"' ~["]*? '"' | '\'' ~[']*? '\'';

FLOAT: [0-9] ('_'? [0-9])* '.' [0-9] ('_'? [0-9]*);
INT: [0-9] ('_'? [0-9])*;

ID: [a-zA-Z_] [_a-zA-Z0-9]*;

LINE_COMMENT: '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;

// Newlines and Spaces are hidden/skipped
NL: [\r\n]+ -> channel(HIDDEN);
WS: [ \t]+ -> skip;