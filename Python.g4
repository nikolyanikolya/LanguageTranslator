grammar Python;
prog: EOF
    | if_statement prog
    | while_statement prog
    | else_statement prog
    | elif_statement prog
    | statement prog
    ;

else_statement: 'else' COLON block_with_tab ;
elif_statement: 'elif' expr COLON block_with_tab ;
block_with_tab: statement_with_tab+ ;
TAB: [\t];
statement_with_tab: TAB* statement ;
TYPE_ID: 'int' ;
left_value: ID ;
ID: [A-Za-z_][A-Za-z0-9_]* ;
EQUAL: [=] ;
INPUT: 'input' LEFT_PAREN RIGHT_PAREN ;
COLON: ':' ;
if_statement: 'if' expr COLON block_with_tab ;
while_statement: 'while' expr COLON block_with_tab ;
LEFT_PAREN: '(' ;
RIGHT_PAREN: ')' ;
PLUS: '+' ;
MINUS: '-' ;
MULTIPLY: '*' ;
DIVIDE: '/' ;
print: 'print' LEFT_PAREN expr RIGHT_PAREN ;
expr:	expr (MULTIPLY|DIVIDE) expr
    |	expr (PLUS|MINUS) expr
    |	INTEGER
    |   ID
    |	LEFT_PAREN expr RIGHT_PAREN
    ;
right_value: INPUT
    |   TYPE_ID LEFT_PAREN right_value RIGHT_PAREN
    |   expr
    ;
statement:	left_value EQUAL right_value
    |	print
    ;
WHITE_SPACE: [\r\n ]+ -> skip;
INTEGER: [0-9]+ ;