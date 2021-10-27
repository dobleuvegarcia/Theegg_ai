import time
lista=[3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56]
lista_ordenada=[]
rango0=len(lista)

def mayor_menor():
	"""vamos a recorrer la lista obteniendo el valor minimo 
	y su indice"""
	for i in range(len(lista)):
		valor=min(lista)
		indice=min(range(len(lista)),key=lista.__getitem__)
		if i ==0:
			"""inicializamos la nueva lista con el valor minimo 
			borramos pasando el indice al valor en la lista inicial"""
			lista_ordenada.insert(0,valor)
			lista.pop(indice)
		else:
			"""anadimos el valor minimo a la lista nueva
			y lo borramos pasando el indice""" 
			lista_ordenada.append(valor)
			lista.pop(indice)

def buscar(num):
	""" vamos a buscar el numero en la lista ya ordenada 
	en la funcion anterior"""
	encontrado=False
	inicio=0#posicion inicial del puntero 
	"""inicializamos fin a numero de elementos de lista_ordenada"""
	fin=len(lista_ordenada)	
	cont=0#inicializamos contador de movimientos
	while not encontrado:
		""" mientras no sea encontrado...
		sumaremos el indice de la primera posicion(inicio) y 
		el indice de la ultima posicion posible(fin) y 
		lo dividimos entre dos: 
		para calcular la posicion entre del puntero entre principio y fin
		del siguiente valor a comparar por cada tramo del bucle."""
		posicion=int((inicio+fin)/2)
		"""un vez hallado el valor de la posicion del medio, preguntamos 
		si el numero dado es mayor, menor o por descarte es igual al valor:

		si numero es mayor al valor que esta en dicha posicion
		calcularemos la siguiente posicion del indice(inicio)
		y sumaremos un movimiento"""
		if num>lista_ordenada[posicion]:
			inicio=posicion+1
			cont+=1
			""" si es menor restaremos uno a la cota o posicion mas alta(fin)
		y sumaremos un movimiento"""
		elif num<lista_ordenada[posicion]:
			fin=posicion-1
			cont+=1
			"""si no cumple ninguna de las demas condiciones 
		entonces es que hemos encontrado el numero a buscar
		y mostramos por pantalla el numero(cont) de movimientos
		o vueltas de bucle hasta encontrarlo. """
		else:
			encontrado=True
			return("encontrado en ",cont," movimientos")





print("lista a ordenar ==>> 3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56")
t0=time.time()
mayor_menor()
t1=time.time()
num=874
solucion=buscar(num)
t2=time.time()
print("lista ya ordenada==>>",lista_ordenada , "---- ordenada en :   {}".format(t1-t0))
print(solucion," ordenada en : {}".format(t2-t1)," segundos")

