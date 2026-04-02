grammar AiLang;

// --- Parser Rules ---

prog: stat+;

block: ARR label? context;

label: '@' id;

context: '{' stat* '}';

// Changed: referenced the Lexer token BOOL_OP correctly
bool_context: '{' bool_group* '}';

bool_group: bool_stat (BOOL_OP bool_stat)*;

assignment: id ':=' expr;

// Added back the 'id' rule since some of your other rules reference it
id: ID;

ref_op: id REF expr;

column_ref_op: column REF expr;

stat:
	func_def		# functionDef
	| assignment	# assign
	| ref_op		# reference
	| column_ref_op	# column_reference
	| expr			# printExpr
	| block			# block_stat
	| doIfElse		# do_if_else
	| fromToData	# load_op;

// Fixed: Corrected the parameter list and ID references
func_def: FUNCTION id REF '(' id (',' id)* ')' context;

fromToData: FROM STR ARR id;

doIfElse: DO context IF bool_context (ELSE context)?;

bool_stat: expr BOOL_OP expr;

expr:
	basic_val			# basicValExpr
	| df				# dataframe
	| column_method		# columnMethod
	| column			# columnID
	| id				# idVal
	| func				# function
	| list				# listValExpr
	| '(' expr ')'		# group
	| expr MATH_OP expr	# mathOp;

named_arg: id '=' expr;

arg: named_arg | expr;

arg_list: '(' (arg (',' arg)*)? ')';

generic_list: '(' expr (',' expr)* ')';

list: basic_list | generic_list | id;

df: '[' df_val (',' df_val)* ']';

df_val: (id ':')? basic_list;

column_id : id | INT;

column: id '.' column_id # simpleColumn | id '.' '@' id # columnSet;

column_method: column '.' id (REF arg_list)?;

func: '.' id (REF arg_list)?;

basic_list:
	'(' num (',' num)* ')'		# numList
	| '(' str (',' str)* ')'	# strList;

basic_val:
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