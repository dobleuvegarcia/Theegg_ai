
import random

class Jugada():
	"""docstring for Baraja"""
	def __init__(self):
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


	def barajar(self,barajado):
		self.__barajado=barajado
		#print(self.__cartas)
		if (self.__barajado):
			baraja=self.__cartas
			self.__barajado=random.sample(baraja,53)
			return(list(self.__barajado))


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
		return(barajados)

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
	def Codificando(self,intercambiado):
		ultima_carta=intercambiado[-1]
		for i in range(len(ultima_carta)):
			if ultima_carta[i]=="Treboles":
				suma=ultima_carta[1]
			elif ultima_carta[i]=="Diamantes":
				suma=ultima_carta[1]+13
			elif ultima_carta[i]=="Corazones":
				suma=ultima_carta[1]+26
			elif ultima_carta[i]=="Picas":
				suma=ultima_carta[1]+39
			elif ultima_carta[i]=="JOKER_A":
				suma=53
			elif ultima_carta[i]=="JOKER_B":
				suma=53
		

jugar=Jugada()
barajados=jugar.barajar(True)
baraja2=barajados
posicionamiento_jokers=jugar.JOKER_A_JOKER_B(barajados)
intercambiado=jugar.Intercambiar(posicionamiento_jokers)
codificar=jugar.Codificando(intercambiado)



