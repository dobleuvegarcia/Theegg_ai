import math

def comparacion_numeros(num1, num2):
	if num1==num2:
		print("estos numeros son iguales")
	elif num1!=num2:
		print("estos numeros son diferentes")
	elif num1>num2:
		print(str(num1)+" es mayor que "+str(num2))
	elif num2>=num1:
		print("El "+str(num2)+"es mayor o igual al numero "+str(num1)