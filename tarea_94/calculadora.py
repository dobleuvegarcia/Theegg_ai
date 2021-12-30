import math

def pedirDatos():
	""" en esta funcion pedimos un numero, si no es entero
	saltara el except y si no devolvera el numero introducido """
	try:
		num=int(input("intruduce un numero"))
	except ValueError:
		print("------------:Error:--------------")
		pedirDatos()
	else:
		return(num)


def pedirOperacion(n1,n2):
	""" En esta funcion pediremos el operador validando si esta en nuestra lista
	si es asi llamaremos a la funcion operacion pasandole el index del operador 
	y los numeros si no es asi saltara la excepcion 
	y volveremos a pedir el operador  """
	lista_operadores=["+","-","*","/"]
	try:
		operador=str(input("introduce el operador de la operacion: +  -  *  /  "))
		op=lista_operadores.index(operador)
		if op==None:
			pedirOperacion(n1,n2)
		else:
			resultado=operacion(n1,n2,op)
			print(resultado)
	except ValueError:
		print("introduce un operador")
		pedirOperacion(n1,n2)
	
	
def operacion(n1,n2,op):
	""" En esta funcion llamaremos a la funcion correspondiente pasandole los numeros
	 dependiendo del index del operador en la lista """
	if op == 0:
		return(suma(n1,n2))
	elif op == 1:
		return(resta(n1,n2))
	elif op == 2: 
		return(multiplicar(n1,n2))
	elif op == 3:
		return(dividir(n1,n2))

#funcion que suma dos numeros dados
def suma(num1,num2):
	result=int(num1 + num2)
	return(result)

#funcion que resta dos numeros dados
def resta(num1,num2):
	result=int(num1) - int(num2)
	return(result)

#funcion que multiplica dos numeros
def multiplicar(num1,num2):
	result=int(num1) * int(num2)
	return(result)

#funcion que divide dos numeros
def dividir(num1,num2):
	try:
		result=int(num1) / int(num2)
		return(result)
	except:
		print("no se puede dividir por 0")
def error():
	print('ERROR: Introduce uno de estos operadores  +  -  *  /   ')