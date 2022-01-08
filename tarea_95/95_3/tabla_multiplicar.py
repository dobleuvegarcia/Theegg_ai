

def pedirDatos():
	""" en esta funcion pedimos un numero, si no es entero...
	saltara el except y si no... devolvera el numero entero introducido """
	num=int(-1)
	try:
		while num<0 or num>99:
			num=int(input("Introduce un numero entre 0 y 99:   "))
		else:
		  	return(num)
	except ValueError:
		print("------------:Error: - Introduce numero entero --------------")
		pedirDatos()
	
def tabla_multiplicar(num,i):
	n=int(num)
	resultado=n*i
	return(resultado)
	