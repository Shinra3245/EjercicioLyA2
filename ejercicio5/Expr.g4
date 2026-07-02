grammar Expr;

root: imprimir EOF;
imprimir: PRINT CADENA;

PRINT: 'print';
CADENA : '"' ~["\r\n]* '"' ;
WS: [ \t\r\n] -> skip;