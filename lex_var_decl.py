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

"""
lexer = lex.lex()
lexer.input(input("Enter : "))
while True :
	tok = lexer.token()
	if not tok :
		break
	print(tok)
"""
