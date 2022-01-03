import numpy
def pedirDatos():
	""" en esta funcion pedimos un numero, si no es entero...
	saltara el except y si no... devolvera el numero entero introducido """
	try:
		num=int(input("Introduce un numero:   "))
	except ValueError:
		print("------------:Error: - Introduce numero entero --------------")
		pedirDatos()
	else:
		return(num)

def comparacion_numeros(num1, num2):
	if num1==num2:
		print("Estos numeros son iguales")
	elif num1!=num2:
		print("Estos numeros son diferentes")
		if num1>num2:
			print(str(num1)+" es mayor que "+str(num2))
	if num2>=num1:
		print("El "+str(num2)+" es mayor o igual al numero "+str(num1))