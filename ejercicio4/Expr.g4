grammar Expr;


root : expr EOF;

// expr : expr MAS expr | NUM;
expr : EOF;

IF: 'if';
ID: [a-zA-Z]+;
MAYOR_QUE: '>';
NUM: [0-9]+;
WS: [ \t\r\n]+ -> skip;