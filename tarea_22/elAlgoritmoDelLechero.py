try:
	num_tot_vacas=int(input("introduce el numero total de vacas de Tolosa que estan a la venta:   "))
	peso_maximo_camion=int(input("introduce el peso maximo que soporta el camion:   "))
	cont=0
	arr=[]
	while num_tot_vacas>cont:
		peso=float(input("introduce el peso de la vaca numero: " +str(cont+1)+"   "))
		diccionario={}
		diccionario['index']=cont
		diccionario['peso'] =peso
		produccion_leche=float(input("introduce la produccion de leche de la vaca numero: " +str(cont+1)+"   "))
		diccionario['leche']=produccion_leche
		r_peso=float(diccionario['peso'])
		r_leche=float(diccionario['leche'])
		total_produccion_vaca=float(r_peso-(r_leche*1.03))
		diccionario['produccion']=total_produccion_vaca
		cont=cont+1
		arr.append(diccionario)
	print(" ------------------------------------------------------------------------------------------- ")
	ordenado=[]
	ordenado=sorted(arr, key=lambda x: x['produccion'])
	#print(str(ordenado))
	peso_totales_vacas=0
	cont=0
	i=0
	produccion_maxima=0
	tot=0
	for i in range(len(ordenado)):
		if peso_totales_vacas<=peso_maximo_camion:
			sum_peso=float(ordenado[i]['peso'])
			sum_leche=float(ordenado[i]['leche'])
			vaca_numero=0
			peso_totales_vacas=float(sum_peso+peso_totales_vacas)
			if peso_totales_vacas<=peso_maximo_camion:
				tot=float(peso_totales_vacas)
				produccion_maxima=float(produccion_maxima+sum_leche)
				vaca_numero=int(ordenado[i]['index']) +1
				print("   Vaca numero  "+str(vaca_numero)+"    aceptada en compra")
				print("   El peso de la vaca es : "+ str(sum_peso)+"  kilogramos")
				print("   La produccion de leche de la vaca es : "+str(sum_leche)+"  litros")
				cont=cont+1
				i=i+1
	print(" ------------------------------------------------------------------------------------------- ")
	print("   Total vacas de mayor produccion que puede llevar el camion es de: "+str(cont)+ "  vacas") 
	print("   Peso total de vacas que puede llevar el camion es : "+str(tot)+ " kilos en vacas") 
	print("   Produccion maxima diaria :  "+ str(produccion_maxima)+ " litros")
except:
	print("introduce bien los parametro fin del programa")