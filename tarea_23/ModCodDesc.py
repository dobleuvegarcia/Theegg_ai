
import random

class Jugada():
	"""docstring for Baraja"""
	def __init__(self,texto):
		self.__abc=[]
		self.__abc=["A","B","C","D","E","F","G","H","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
		self.__palo = ("Treboles","Diamantes","Corazones","Picas")
		self.__num = (1,2,3,4,5,6,7,8,9,0,11,12,13)
		self.__cartas=[]
		for p in range(len(self.__palo)):
			for n in range(len(self.__num)):
				pc=self.__palo[p]
				nc=self.__num[n]
				self.__cartas.append([pc,nc])

		self.__cartas.append(["JOKER_A",53])
		self.__cartas.append(["JOKER_B",53])
		self.__barajado=False
		self.__cartas=self.barajar(True)
		self.__baraja2=self.__cartas

		self.__cartas=self.JOKER_A_JOKER_B(self.__cartas)

		self.__cartas=self.Intercambiar(self.__cartas)

		suma=self.SumaUltimaCarta(self.__cartas)
		#print(self.__cartas)
		self.estado_baraj_final_suma=self.CorteSuma(suma, self.__cartas)
		self.__cartas=self.estado_baraj_final_suma[0]

		self.__texto=texto.upper()
		#print(self.__texto)
		self.__num=[]
		for i in range(len(self.__texto)):
			for a in range(len(self.__abc)):
				if self.__texto[i]==self.__abc[a]:
					numero=self.__abc.index(self.__abc[a])
					numero=numero+1

					self.__num.append([self.__texto[i],numero])
		#print(self.__num)


    #esta funcion barajea las cartas
	def barajar(self,barajado):
		self.__barajado=barajado
		#print(self.__cartas)
		if (self.__barajado):
			baraja=self.__cartas
			self.__cartas=random.sample(baraja,53)
			return(list(self.__cartas))



	


	#esta funcion posiciona los jokers a y b segun el solitario pasandole la baraja ya barajeada
	def JOKER_A_JOKER_B(self,barajados):
		for j_a in range(len(barajados)):
			if (barajados[j_a][0]=="JOKER_A"):
				old_index = barajados.index(barajados[j_a])
				if old_index==53:
					new_index=1
					#print(new_index)
					itm=barajados[j_a]
					barajados.remove(itm)
					barajados.insert(new_index, itm)
					#print(old_index, itm, new_index)
					break;
				else:	
					new_index=old_index+1
					#print(new_index)
					itm=barajados[j_a]
					barajados.remove(itm)
					barajados.insert(new_index, itm)
					#print(old_index, itm, new_index)
					break;
		
		for j_b in range(len(barajados)):
			if (barajados[j_b][0]=="JOKER_B"):
				old_index = barajados.index(barajados[j_b])
				if old_index==53:
					new_index=2
					#print(new_index)
					itm=barajados[j_a]
					barajados.remove(itm)
					barajados.insert(new_index, itm)
					#print(old_index, itm, new_index)
					break;
				elif old_index==52:
					new_index=1
					#print(new_index)
					itm=barajados[j_a]
					barajados.remove(itm)
					barajados.insert(new_index, itm)
					#print(old_index, itm, new_index)
					break;

				else:
					new_index=old_index+2
					#print(new_index)
					itm=barajados[j_b]
					barajados.remove(itm)
					barajados.insert(new_index, itm)
					#print(old_index, itm, new_index)
					break;
		#print(barajados)
		return(barajados)


	#esta funcion parte la baraja en tres teniendo la particion de el medio separada por joker a y 
	#y joker b pasando la primera particion abajo y la tercera arriba dejando la mitad en medio
	def Intercambiar(self,pos_jokers):
		corte1=[]
		corte2=[]
		corte3=[]
		
		for j in range(53):
			if pos_jokers[j][1]!=53:
				carta=pos_jokers[j]
				corte1.append(carta)
			else:
				i=pos_jokers.index(pos_jokers[j])
				corte2.insert(0,pos_jokers[j])
				#print(i)
				x=i+1
				break;
		#print(corte1)
		for i in range(x,53):
			#print(i)
			if pos_jokers[i][1]!=53:
				carta=pos_jokers[i]
				corte2.append(carta)
			else:
				x=pos_jokers.index(pos_jokers[i])
				corte2.insert(x,pos_jokers[i])
				x=x+1
				break;
		#print(corte2)
		for o in range(x,53):
			if pos_jokers[o][1]!=53:
				carta=pos_jokers[o]
				corte3.append(carta)
			else:
				break;
		#print(corte3)
		intercambiadas=[]
		for inter in range(len(corte3)):
			intercambiadas.append(corte3[inter])
		for inter in range(len(corte2)):
			intercambiadas.append(corte2[inter])
		for inter in range(len(corte1)):
			intercambiadas.append(corte1[inter])
		return(intercambiadas)

	#calculo la suma de la ultima carta
	def SumaUltimaCarta(self,intercambiado):
		ultima_carta=intercambiado[-1]
		suma=self.CalcularSuma(ultima_carta)
		return(suma)


	#contamos las cartas dde la suma y posicionamos el taco de cartas contadas detras de el taco restante
	#y delante de la ultima carta
	def CorteSuma(self,suma,baraja):
		baraja_corte_suma=[]
		#print(baraja)
		#print(suma)
		for i in range(0,suma):
			#print(baraja_corte_suma.append(baraja[i]))
			baraja_corte_suma.append(baraja[i])
			#baraja.remove(baraja[i])
		corte_frontal=[]
		ultima_carta=(baraja[-1])
		#baraja.remove(baraja[-1])	
		for b in range(len(baraja)):
			corte_frontal.append(baraja[b])
		for b in range(len(baraja_corte_suma)):
			corte_frontal.append(baraja_corte_suma[b])
		corte_frontal.append(ultima_carta)
		primera_carta=corte_frontal[0]
		suma=self.CalcularSuma(primera_carta)
		return(corte_frontal,suma)


	#esta funcion calcula la suma dependiendo de el palo
	def CalcularSuma(self,carta):
		for i in range(len(carta)):
			if carta[i]=="Treboles":
				suma=carta[1]
			elif carta[i]=="Diamantes":
				suma=carta[1]+13
			elif carta[i]=="Corazones":
				suma=carta[1]+26
			elif carta[i]=="Picas":
				suma=carta[1]+39
			elif carta[i]=="JOKER_A":
				suma=53
			elif carta[i]=="JOKER_B":
				suma=53
		return(suma)




	#esta funcion repite los pasos anteriores segun la longitud del texto
	def Repetir(self):
		for t in range(len(self.__num)):

			self.__cartas=self.JOKER_A_JOKER_B(self.__cartas)
			self.__cartas=self.Intercambiar(self.__cartas)
			suma=self.SumaUltimaCarta(self.__cartas)
			#print(suma)
			#print(intercambiado)
			ultimo_paso_baraja=self.CorteSuma(suma, self.__cartas)
			#aqui colocar suma al primer valor de letra
			self.__num[t].append(ultimo_paso_baraja[1])
			self.__cartas=ultimo_paso_baraja[0]
		#print(self.__num)
		#print(ultimo_paso_baraja[0])

	def ObtenerLetraCodigo(self):
		for i in range(len(self.__num)):
			num=self.__num[i][1]+self.__num[i][2]
			if num>=53:
				num=num-52
			else:
				num=num-26
			self.__num[i].append(num)
		#print(self.__num)
		codigo=""
		for i in range(len(self.__num)):
			for a in range(len(self.__abc)):
				numero=self.__abc.index(self.__abc[a])
				numero = numero+1
				if (self.__num[i][3]==numero or self.__num[i][3]==-numero):
					letra=self.__abc[a]
					self.__num[i].append(letra)
					codigo=codigo+letra
		#print(self.__num)
		#print(codigo)
		return(codigo)
	def decodificar(self):
		
		pass








