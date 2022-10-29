grammar Python;
prog: <EOF>
    | statement prog
    ;
TYPE_ID: 'int' ;
left_value: ID ;
ID: [A-Za-z_][A-Za-z0-9_]* ;
EQUAL: [=] ;
INPUT: 'input' LEFT_PAREN RIGHT_PAREN ;
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