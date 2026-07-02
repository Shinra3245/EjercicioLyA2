grammar Expr;


root : expr EOF;

// expr : expr MAS expr | NUM;
expr : EOF;

INT: 'int';
ID: [a-zA-Z]+;
IGUAL: '=';
NUM: [0-9]+;
WS: [ \t\r\n]+ -> skip;