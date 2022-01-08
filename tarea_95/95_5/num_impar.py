import math
def pedirDatos():
	""" en esta funcion pedimos un numero, si no es entero...
	saltara el except y si no... devolvera el numero entero introducido """
	num=0
	try:
		while num % 2 == 0:
			num=int(input("Introduce un numero impar   "))
		else:
		  	return(num)
	except ValueError:
		print("------------:Error: - Introduce numero impar --------------")
		pedirDatos()