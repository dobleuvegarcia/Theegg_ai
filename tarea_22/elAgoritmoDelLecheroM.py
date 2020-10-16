import itertools

#creo una funcion para pedir los datos y lo meto en un try 
def PedirDatos():
	try:
		cont=0
		arr=[]
		while num_tot_vacas>cont:
			peso=float(input("introduce el peso de la vaca numero: " +str(cont+1)+"   "))
			diccionario={}
			produccion_leche=float(input("introduce la produccion de leche de la vaca numero: " +str(cont+1)+"   "))
			if produccion_leche > peso -10:
				try:
					chivato=True 
					while chivato==True:
						produccion_leche=float(input("introduce la produccion de leche de la vaca numero: " +str(cont+1)+" Recuerda que una vaca no puede pesar mas que lo que produce ya que un litro=1,03 kilos  ademas dejale al menos 10 kilos de carne y huesos para ser mas real  : "))
						if produccion_leche <= peso -10:
							chivato=False
				except:
					print("introduce bien los parametros fin del programa")
			diccionario[0]=int(cont)
			diccionario[1]=float(peso)
			diccionario[2]=float(produccion_leche)
			
			arr.append(diccionario)
			cont=cont+1
		return(arr)
	except:
		print("debes introducir bien los datos")
#importo la clase itertools pra poder crear todas las combinaciones posibles el TodasCombinaciones()
#paso por parametro el numero total de vacas que hay por la zona 

def TodasCombinaciones (num_tot_vacas):
	#aqui vamos a hallar todas las combinaciones que hay posibles 
	todas_combinaciones=list(itertools.product([0,1],repeat=num_tot_vacas))
	return(todas_combinaciones)
#en esta funcion solo valoro las que sumando todos los pesos de esa combinacion no superen
#el peso del camion
def combinaciones_aceptadas(tot_posb_comb, arr_datos,num_tot_vacas,peso_maximo_camion):

	cont=0
	i=0
	list_opciones=[]
	peso_total=0
	x=0
	campo_linea=[]
	b=[]
	#recorro todas las posibilidades de combinaciones
	for comb_aceptadas in range(len(tot_posb_comb)):
		campo_linea=tot_posb_comb[comb_aceptadas]
		#print("posibilidad: ", campo_linea)
		sum_leche=0
		sum_peso=0
		numeros_vaca=[]
		#recorro los campos por cada posibilidad
		for comb_a in range(len(campo_linea)):
			#si el campo [i] es 01 
			if (campo_linea[comb_a]==1):

				chivato=campo_linea[comb_a]
				#print("campo de lines : ", chivato)
				#recorro el archivo por cada posibilidad de 1 
				for i in range(len(arr_datos)):
					#si coicide el campo_posibilidad :[i]con la posicion index del 1 guardo los datos 
					if i==comb_a:
						vaca=arr_datos[i][0]
						#print("index: ",arr_datos[i][0])
						peso=arr_datos[i][1]
						leche=arr_datos[i][2]
						#print("peso:  " ,peso)
						#print("leche:  " ,leche)
						sum_peso=sum_peso+peso
						sum_leche=sum_leche+leche
						datos_x_posib=[vaca,peso,leche]
						numeros_vaca.append(datos_x_posib)
					
		if sum_peso<=peso_maximo_camion:
			b=[sum_peso,sum_leche,numeros_vaca]
			#print("total peso de esta opcion : ", sum_peso)
			#print("total leche de maxima produccion de esta opcion : ", sum_leche)
			list_opciones.append(b)
	return(list_opciones)

def optimizacion(arr_comb_posib):
	#ordenado=sorted(arr_comb_posib, key=lambda x: x[1], reverse=True)

	print("array combinaciones posibles",arr_comb_posib)
	#num_posibilidades=count(max(arr_comb_posib, key=lambda x: x[1]))

	max_produccion_leche=max(arr_comb_posib, key=lambda x: x[1])
	#for k in max_produccion_leche:
		#print("linea maxima produccion",k)
		#num_posibilidades=len(max_produccion_leche)
	#print("array max leche",max_produccion_leche)
	return(max_produccion_leche)

num_tot_vacas=int(input("introduce el numero total de vacas de Tolosa que estan a la venta:   "))
peso_maximo_camion=int(input("introduce el peso maximo que soporta el camion:   "))
arr_datos=PedirDatos()
#print(arr_datos)
print(" ------------------------------------------------------------------------------------------- ")

todas_posibles_combinaciones=TodasCombinaciones(num_tot_vacas)

combinaciones_Validas=combinaciones_aceptadas(todas_posibles_combinaciones, arr_datos,num_tot_vacas,peso_maximo_camion)
#print("todas posibles combinaciones",todas_posibles_combinaciones)	
posibles_compras=optimizacion(combinaciones_Validas)

for p_c in range(len(posibles_compras)):
	if p_c==0:
		print("total peso : ",posibles_compras[p_c])
	elif p_c==1:
		print("total leche : ",posibles_compras[p_c])
	else:
		for impli in posibles_compras[p_c]:
			num_v=impli[0]
			peso_v=impli[1]
			leche_v=impli[2]
			print("vacas implicadas numero  : ",num_v+1)
			print("peso implicadas : ",peso_v)
			print("leche implicadas : ",leche_v)
	#for t in range(len(lineas_final)):

print(" ------------------------------------------------------------------------------------------- ")


