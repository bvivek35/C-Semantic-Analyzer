import ply.lex as lex
import ply.yacc as yacc

from lexer import *
from parser import *

lexer = lex.lex()
parser = yacc.yacc()
res = parser.parse(input('Enter String : '))
print(res)
