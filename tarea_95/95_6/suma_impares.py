def suma_impar():
	num=0
	for i in range(115):
		if i%2!=0:
			num=num+i
	print("El resultado de la suma de impares de 0 hasta 115 es:"+str(num))

suma_impar()