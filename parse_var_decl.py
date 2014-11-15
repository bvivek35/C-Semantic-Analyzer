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

