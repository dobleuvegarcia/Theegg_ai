
import random

class Jugada():
	"""docstring for Baraja"""
	def __init__(self):
		self.__abc=[]
		self.__abc=["A","B","C","D","E","F","G","H","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
		self.__palo = ("T","D","C","P")
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
				else:
					new_index=old_index+2
					#print(new_index)
					itm=barajados[j_b]
					barajados.remove(itm)
					barajados.insert(new_index, itm)
					#print(old_index, itm, new_index)
					break;
		return(barajados)

	def intercambiar(self,pos_jokers):
		pass

jugar=Jugada()

barajados=jugar.barajar(True)
baraja2=barajados
posicionamiento_jokers=jugar.JOKER_A_JOKER_B(barajados)
intercambiado=intercambiar(posicionamiento_jokers)



