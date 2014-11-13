import ply.lex as lex
import ply.yacc as yacc



tokens = [
	'INT',
	'FLOAT',
	'DOUBLE',
	'CHAR',
	'ID',
	'SEMICOLON',
	'ASSIGN',	
	]

reserved = {
	'int' : 'TYPE_INT',
	'float' : 'TYPE_FLOAT',
	'double' : 'TYPE_DOUBLE',
	'char' : 'TYPE_CHAR',		
	}

tokens = tokens + list(reserved.values())


t_INT = r'[+-]?\d+'
t_DOUBLE = r'[+-]?\d+\.\d+'
t_FLOAT = r'[+-]?\d+\.\d+f'
t_CHAR = r'\'[\w]\''

def t_ID(t) :
	r'[_a-zA-Z][\w_]*'
	t.type = reserved.get(t.value, 'ID')
	return t		


t_SEMICOLON = r';'
t_ASSIGN = r'='

t_ignore = " \n\t"

lexer = lex.lex()
"""lexer.input(input("Enter : "))
while True :
	tok = lexer.token()
	if not tok :
		break
	print(tok)
"""
def p_var_decl(p) :
	''' var_decl : type ID SEMICOLON
		     | type ID ASSIGN value SEMICOLON'''
	print(type(p))
	if len(p) == 6 :
		p[0] = p[4]		
	else :
		p[0] = p[1]
	print('var decl')

def p_type(p) :
	'''type : TYPE_INT
		| TYPE_FLOAT
		| TYPE_CHAR
		| TYPE_DOUBLE'''
	p[0] = p[1]	
	print('type')
	
def p_value(p) :
	'''value : INT
		 | FLOAT
		 | DOUBLE
		 | CHAR
		 | ID'''
	p[0] = p[1]					
	print('value')


parser = yacc.yacc()
res = parser.parse(input("Enter : "))
print(res)

