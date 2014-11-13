import ply.lex as lex
import ply.yacc as yacc

tokens = (
	'INT',
	'FLOAT',
	'DOUBLE',
	'CHAR',
	'ID',
	'SEMICOLON'	
	)

t_INT = r'[+-]?\d+'
t_DOUBLE = r'[+-]?\d+\.\d+'
t_FLOAT = r'[+-]?\d+\.\d+f'
t_CHAR = r'\'[\w]\''
t_ID = r'[_a-zA-Z][\w_]*'
t_SEMICOLON = r';'

t_ignore = " \n\t"

lexer = lex.lex()
lexer.input(input("Enter : "))
while True :
	tok = lexer.token()
	if not tok :
		break
	print(tok)

