import time
lista=[3, 56, 21, 33, 874, 123, 66, 1000, 23, 45, 65, 56]
lista_ordenada=[]
rango0=len(lista)

def mayor_menor():
	for i in range(len(lista)):
		valor=min(lista)
		posicion=min(range(len(lista)),key=lista.__getitem__)
		if i ==0:
			lista_ordenada.insert(0,valor)
			lista.pop(posicion)
		else:
			lista_ordenada.append(valor)
			lista.pop(posicion)

def buscar(num):
	encontrado=False
	inicio=0
	fin=len(lista_ordenada)
	cont=0
	while not encontrado:
		posicion=int((inicio+fin)/2)
		if num>lista_ordenada[posicion]:
			inicio=posicion+1
			cont+=1
		elif num<lista_ordenada[posicion]:
			fin=posicion-1
			cont+=1
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

