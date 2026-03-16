grammar AiLang;

prog: stat+;
block: ARR label? context;
label: '@' ID;
context: '{' stat* '}';

bool_context: '{' NL* bool_group (NL NL+ bool_group)* NL* '}';
bool_group: bool_stat (NL* bool_op NL* bool_stat)*;

assignment:    id ':=' expr NL;
ref_op:        id     REF NL? expr NL?
             | id     NL+  REF NL? expr NL?
             ;
column_ref_op: column REF NL? expr NL?
             | column NL+  REF NL? expr NL?
             ;

stat: func_def          #functionDef
    | assignment        #assign
    | ref_op            #reference
    | column_ref_op     #column_reference
    | expr NL           #printExpr
    | NL                #blank
    | block             #block_stat
    | doIfElse          #do_if_else
    | fromToData        #load_op
    ;

DO:       'do';
IF:       'if';
ELSE:     'else';
FROM:     'from';
FUNCTION: 'function';

func_def: FUNCTION ID REF '(' ID (',' ID)* ')' context NL?;

fromToData: FROM STR ARR ID;

doIfElse: DO context IF bool_context (ELSE context)?;

bool_stat: expr bool_op expr;

MATH_OP: '+' | '-' | '*' | '/';

expr: basic_val             #basicValExpr
    | df                    #dataframe
    | column_method         #columnMethod
    | column                #columnID
    | id                    #idVal
    | func                  #function
    | list                  #listValExpr
    | '(' expr ')'          #group
    | expr MATH_OP expr     #mathOp
    ;

named_arg: ID '=' expr;
arg: named_arg
   | expr
   ;
arg_list: '(' arg (',' arg)* ')';

list: basic_list
    | '(' expr (',' expr)* ')'
    | id
    ;

df: '[' df_val (',' df_val)* ']';
df_val: (ID ':')? basic_list;

column: ID '.' ID     #simpleColumn  
      | ID '.' '@'ID  #columnSet
        ;
column_method: column '.' ID (NL* REF NL? arg_list)?;

// func absorbs its arg_list via <- which may be on the next line
func: '.' ID (NL* REF NL? arg_list)?;

basic_list: '(' num (',' num)* ')' #numList
          | '(' str (',' str)* ')' #strList
          ;

basic_val: num               #number
         | str               #string
         | '(' basic_val ')' #group_basic_val
         ;

num: INT   #intigerLiteral
   | FLOAT #floatLiteral
   ;

str: STR;

STR: '"' ~["]*? '"'
   | '\'' ~[']*? '\''
   ;

FLOAT: INT+ ('.' INT+)?;
INT:   [0-9] ('_'? [0-9])*;

LINE_COMMENT:  '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
NL:    '\r'? '\n';

ARR: '->';
REF: '<-';
id: ID;
ID: [a-zA-Z_] [_a-zA-Z0-9]*;
WS: [ \t] -> skip;

bool_op: BOOL_OP;
BOOL_OP: '>' | '<' | '==' | '&' | '|';
