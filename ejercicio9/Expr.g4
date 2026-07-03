grammar Expr;


root : expr EOF;

// expr : expr MAS expr | NUM;
expr : EOF;

IF: 'if';
PAR_I: '(';
PAR_F: ')';
ID: [a-zA-Z]+;
SIGNO_MA: '>';
IGUAL: '=';
NUM: [0-9]+;
WS: [ \t\r\n]+ -> skip;