try:
	num_tot_vacas=int(input("introduce el numero total de vacas de Tolosa que estan a la venta:   "))
	peso_maximo_camion=int(input("introduce el peso maximo que soporta el camion:   "))
	cont=0
	arr=[]
	while num_tot_vacas>cont:
		peso=float(input("introduce el peso de la vaca numero: " +str(cont+1)+"   "))
		#creo un diccionario de datos e introduzco los datos de consola al diccionario
		diccionario={}
		diccionario['index']=cont #tambien creo una clave index numerica
		diccionario['peso'] =peso
		produccion_leche=float(input("introduce la produccion de leche de la vaca numero: " +str(cont+1)+"   "))
		diccionario['leche']=produccion_leche
		r_peso=float(diccionario['peso'])
		r_leche=float(diccionario['leche'])
		total_produccion_vaca=float(r_peso-(r_leche*1.03))#un litro de leche equivale a 1.03 kilos 
		#le resto los litros a los kilos de la vaca par ver si produce mucho o solo es carne y poca leche
		diccionario['produccion']=total_produccion_vaca # aqui guardo la relacion de carne-leche en el cuerpo
		cont=cont+1
		arr.append(diccionario)#añado el diccionario al array de diccionarios
	print(" ------------------------------------------------------------------------------------------- ")
	ordenado=[]
	ordenado=sorted(arr, key=lambda x: x['produccion']) #ordeno el array por kilos de carne en el cuerpo ascendente dando asi de mayor a menor la leche en el cuerpo
	#print(str(ordenado)) chivato 
	peso_totales_vacas=0
	cont=0
	i=0
	produccion_maxima=0
	tot=0
	#print(str(len(ordenado)))
	for i in range(len(ordenado)):
		sum_peso=float(ordenado[i]['peso'])
		sum_leche=float(ordenado[i]['leche'])
		peso_totales_vacas=float(sum_peso+peso_totales_vacas)#sumo los pesos acumulados
		if peso_maximo_camion>=peso_totales_vacas: #comparo si es menor los kilos acumulados con el maximo del camion
			vaca_numero=0
			tot=float(peso_totales_vacas)
			produccion_maxima=float(produccion_maxima+sum_leche) #guardo en la variable los acumulados de leche que puede llevar el camion
			vaca_numero=int(ordenado[i]['index']) +1 #numero de la vaca seleccionada +1 ya que comienza por 0
			print("   Vaca numero  "+str(vaca_numero)+"    aceptada en compra")
			print("   El peso de la vaca es : "+ str(sum_peso)+"  kilogramos")
			print("   La produccion de leche de la vaca es : "+str(sum_leche)+"  litros")
			cont=cont+1
			i=i+1
		else:
			peso_totales_vacas=float(peso_totales_vacas-sum_peso)#resto el ultimo peso acumulado

	print(" ------------------------------------------------------------------------------------------- ")
	print("   Total vacas de mayor produccion que puede llevar el camion es de: "+str(cont)+ "  vacas") 
	print("   Peso total de vacas que puede llevar el camion es : "+str(tot)+ " kilos en vacas") 
	print("   Produccion maxima diaria :  "+ str(produccion_maxima)+ " litros")
except:
	print("introduce bien los parametro fin del programa")