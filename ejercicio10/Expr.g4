grammar Expr;


root : expr EOF;

// expr : expr MAS expr | NUM;
expr : EOF;

PRINT: 'print';
CADENA: '"'~["\r\n]*'"';
PAR_IZQ: '(';
PAR_DER: ')';
PUNTO_COMA: ';';
WS: [ \t\r\n]+ -> skip;