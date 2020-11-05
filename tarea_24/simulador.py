import itertools

def Conversor(num):
	#convierto el numero a entero redondeando
	numEntero=round(num)
	restoAcumulado=[]
	binario=""
	#mientras el numero sea mayor k 0 sigo obteniendo el resto y acumulandolo en el array..
	while (numEntero>0):
		resto=numEntero % 2
		restoAcumulado.append(resto)
		numEntero=int(numEntero/2)
		#si el resto es uno añado ese uno al codigo binario en el ultimo lugar
		if numEntero==1:
			restoAcumulado.append(numEntero)
			break;
	#muestro el array del reves para obtener el codigo binario
	for b in reversed(restoAcumulado):
		binario=binario+str(b)
	return(binario)