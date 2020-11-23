import ply.yacc as yacc
from lexer import tokens


def p_expresion(p):
    '''expresion : expresiones
    | funcion
    '''

def p_expresiones(p):
    '''expresiones : lista
    | mapa
    | variable
    | concatenacion
    | incremento
    | decremento
    | print
    '''

# Juan Nebel
def p_variable(p):
    '''variable : VAR ID EQUALS expresionVar PUNTCOM
                | VAR ID PUNTCOM
                | expresionBool'''

def p_valorVar(p):
    '''valorVar : NUMBER
                | DOUBLE
                | CADENA'''

def p_expresionVar(p):
    '''expresionVar : valorVar
                    | ID 
                    | expresionVar operadorA expresionVar'''

#Allison Brito y JF Nebel
def p_expresionBool(p):
    '''expresionBool : VARBOOL ID EQUALS booleano pto_coma
                     | VAR ID EQUALS booleano pto_coma''' 

def p_booleano(p):
    '''booleano : TRUE
    | FALSE'''

#Allison Brito
#Regla de expresion de lista
def p_lista(p):
    '''lista : expLista
    | add_lista
    '''
#Inicializacion de una lista
def p_expLista(p):
    '''expLista : VAR ID EQUALS NEW LISTA LPAREN inicializaLista RPAREN pto_coma
        | VAR ID EQUALS LCORCHETE elementosLista RCORCHETE pto_coma
        '''
#Valor que se le asigna al momento de declarar el # de elementos de un mapa
def p_inicializaLista(p):
    '''inicializaLista  : NUMBER
    | 
    '''

#Agregar elementos a una lista
def p_add_lista(p):
    '''add_lista : ID LCORCHETE NUMBER RCORCHETE EQUALS num_cadena pto_coma
    | ID PTO ADD LPAREN num_cadena RPAREN pto_coma
    '''
#Toma el valor de un numero o de un string con comillas incluido
def p_num_cadena(p):
    '''num_cadena : NUMBER
    | CADENA'''

#Recursividad al agregar elementos de una lista
def p_elementosLista(p):
    '''elementosLista : CADENA
        | NUMBER
        | CADENA COMA elementosLista
        | NUMBER COMA elementosLista
        | 
    '''
#Operaciones en un mapa: inicializar y agregar elemento
def p_mapa(p):
    '''mapa : expMapa
    | add_mapa
    '''
#Inicializacion de un mapa
def p_expMapa(p):
    '''expMapa : VAR ID EQUALS NEW MAPA LPAREN RPAREN pto_coma
    | MAPA ID EQUALS LCURLYB elementosMapa RCURLYB pto_coma
    '''

#Recursividad al agregar elementos de un mapa
def p_elementosMapa(p):
    '''elementosMapa : num_cadena DOSPTO num_cadena
    | num_cadena DOSPTO num_cadena COMA elementosMapa
    '''

#Agrega a la ED mapa
def p_add_mapa(p):
    '''add_mapa : ID LCORCHETE CADENA RCORCHETE EQUALS CADENA pto_coma
    '''

def p_operadorA(p):
    '''operadorA : PLUS
    | MINUS
    | TIMES
    | DIVIDE
    | DIVIDE_E
    '''

def p_incremento(p):
    'incremento : ID INCREMENTO pto_coma'

def p_decremento(p):
    'decremento : ID DECREMENTO pto_coma'


#Metodo substing de un string
def p_concatenacion(p):
    '''concatenacion : VAR ID EQUALS ID PTO SUBSTRING LPAREN NUMBER COMA NUMBER RPAREN pto_coma
    '''
#Imprimir datos
def p_print(p):
    '''print : PRINT LPAREN printVal RPAREN pto_coma
    '''

def p_printVal(p):
    '''printVal : ID
    | valorVar
    '''

#Construir una funcion
def p_funcion(p):
    '''funcion : VOID ID LPAREN RPAREN LCURLYB expresiones RCURLYB
    '''

#regla de punto y coma
def p_pto_coma(p):
    'pto_coma : PUNTCOM'

def p_error(p):
    print("Syntax error in input!",p)




# Build the parser
parser = yacc.yacc()
 
while True:
    try:
        s = input('Ingrese el codigo > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
