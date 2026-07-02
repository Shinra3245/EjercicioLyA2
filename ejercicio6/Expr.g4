grammar Expr;

root : expresion EOF ;
expresion : (NUM | SUM | SIGNO)+ ;

NUM   : [0-9]+ ;
SUM   : '+' ;
SIGNO : '*' ;
WS    : [ \t\r\n]+ -> skip ;