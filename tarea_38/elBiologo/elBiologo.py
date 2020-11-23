#En este programa vamos testear los maximos adyacentes comunes a dos cadenas de ADN.
import itertools
import random
import re
class Nucleotidos():
	"""Creamos una clase llamada Nucleotidos que se inicializa 
	con la tabla de "numenclatura" y nucleotidos 
	tiene dos metodos:
	1ª metodo RndAdn crea dos secuencias de adn aleatorias de longitud 13
	2ª metodo Nu_comparate compara los nucleotidos posibles 
	en las dos secuencias de ADN 
	dando como resultado los adyacentes o comunes entre si de maxima longitud"""

	def __init__(self):
		self.nucleotidos=["Adenina","Citosina","Guanina","Timina"]
		self.nomcl=self.Iniciales()

		#creamos una tabla con las nomenclaturas de la tabla nucleotidos
		#con la cual trabajaremos para la comparacion de las cadenas de adns
	def Iniciales(self):
		nomcl=""
		for i in range(len(self.nucleotidos)):
			#llamada a la primera letra de  tabla nucleotidos
			nom=next(self.Nomenclatura(self.nucleotidos[i])) 
			nomcl+=nom#acumulamos cada inicial
		return(nomcl)

	def Nomenclatura(self,nucl):
		# devuelve la primera inicial de la lista nucleotidos
		for n in nucl:
				yield from n

	# funcion que crea las dos secuencias aleatorias de ADN de long 13
	def RndAdn(self):
		c=self.nomcl
		adn=""
		for n in range(13):#hasta rango 13
			a=random.choice(c)#elige una letra cualquiera de c(self.nomencl)
			adn+=a#acumula la letra de la var(a) creando secuencia en adn
		#devolvemos una secuencia de adn rango 13
		return(adn)
 
	#comparacion de las dos cadenas de ADN
	def Nu_comparate(self, adn1,adn2):
		comunes = set(adn1).intersection(set(adn2))
		l_ady1=0
		l_ady2=0
		ady_l=""
		adyacentes=""
		pc_ady=[]
		cont=2
		for c in comunes:#por cada nucleotido en comun:
			#print(c)
			l_ady1+=adn1.count(c)#num por nucleotidos comunes en adn1
			l_ady2+=adn2.count(c)#num por nucleotidos comunes en adn2
			l_ady=min(l_ady1,l_ady2)#long max de secuencia=minima en comun
			ady_l+=c#cadena letras de nucleotidos
			for l in range(l_ady):#en el rango de secuencia maxima en comun
			#hallamos las posibles combinaciones de nucleotidos (ady_l)
			#desde cont=2 parejas hasta que cont=l_ady (rango de secuencia maxima en comun)
				pos_comb_ady=list(itertools.product(ady_l, repeat=cont))
			cont+=1
		#recorremos las posibles combinaciones adyacentes
		ady=0#inicialiar la longitud maxima del patron en cadenas de adn
		for p in range(len(pos_comb_ady)):
			patron=""#inicializar/limpiar nomenclaturas, nucleotidos en comun
			for p1 in pos_comb_ady[p]:#sacamos la primera posible combinacion adyacente
				patron+=p1#añadimos las numenclaturas para sacar el patron
				#buscamos el patron en adn1 de las posibles combinaciones
				a1=re.findall(patron, adn1)
				#buscamos el patron en adn2 de las posibles combinaciones
				a2=re.findall(patron, adn2)
				#extraemos el patron de a1(n) y a2(h) encontrados
				#recorremos para saber si es igual en los adns
				if a1 and a2:#si los patrones son iguales
					y=len(patron)#hallamos la longitud
					if y>ady:#comparamos si la longitud es mayor a la encontrada
						ady=y#guardamos la longitud mas larga
						adyacentes=patron#guardamos la secuencia de longitud maxima

			

"""solo visualizar por pantalla, para correccion.
			 muestra cadena de nucleotidos en comun con los 2 ADNs. 
			 podria haber nucleotidos que no existen en alguna
			 cadena de ADN y son excluidos de posibles combinaciones._______
			 _______________________________________________________
		print("buscar: NUCLEOTIDOS COMUNES en 2 ADNs :  ",ady_l)
		print(" LONG MAX ADYACENTES POSIBLES : " ,l_ady)_______"""

		return(adyacentes)

nu=Nucleotidos()
#creo la lista adn1 y adn2 aleatoria
adn1=nu.RndAdn()
adn2=nu.RndAdn()
ady=nu.Nu_comparate(adn1,adn2)


""" APARTADO SOLO PARA LA CORRECCION DE LOS DATOS Y VISUALIZACION
POR PANTALLA. 
EN ESTE EJERCICIO SOLO SE PIDE EJECUCION NI ENTRADA NI DALIDA DE DATOS:
 desactivar las comillas SOLO para LA DEMOSTRACION 
 Y VISUALIZACION DE PANTALLA DE RESULTADOS:
 _________________________________________________________

print("1ª ADN ALEATORIO:  ",adn1)
print("2ª ADN ALEATORIO:  ",adn2)
print("RELSUTADO MAXIMOS ADYACENTES EN AMBOS ADNs:" ,ady)__"""

