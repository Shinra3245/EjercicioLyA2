grammar Expr;

root: expr EOF;

expr: EOF;

ID: [a-zA-Z]+;
NUM: [0-9]+;
IGUAL: '=';
WS: [ \t\r\n] -> skip;
