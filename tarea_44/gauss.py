import time
def suma_lineal(n):
	#suma lineal(n)numero total de numeros a sumar de 1 hasta n ascendente
	suma=0
	for i in range(1,n+1):
		suma+=i
	return(suma)
def suma_constante(n):
	#suma_constante(n)formula de Gauss:
	return((n/2)*(n+1))
#vamos a calcular 4 veces el tiempo de ejecucion de cada funcion 
#inicializando la cantidad en 1000000 y multipicandola cada vez por 10.
cantidad=1000000
for i in range(4):
	t0=time.time()
	suma1=suma_lineal(cantidad)
	t1=time.time()
	suma2=suma_constante(cantidad)
	t2=time.time()
	print("{}-{}".format(suma1,t1-t0))
	print("{}-{}".format(suma2,t2-t1))
	cantidad+=10