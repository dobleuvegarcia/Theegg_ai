from io import open
import re
from itertools import groupby

class rankingText():
	"""En este algoritmo abrimos un archivo para recorrerlo y buscar
	 las 10 palabras mas usadas"""
	def __init__(self):#inicializamos pidiendo el archivo
		ob=(input("Introduce el nombre de archivo y extension:  "))
		txt=self.abrirArchivo(ob)#llamamos a abrir archivo
		result=self.contWord(txt)#llamamos a contword
		print(result)
	
	def abrirArchivo(self,ob):#abrimos archivo
		o=ob
		archivo_texto=open(o,"r",encoding="utf-8")
		txtAnalizar=archivo_texto.read()#guardamos archivo en txtAnalizar

		archivo_texto.close()
		return(txtAnalizar)

	def txtSeparator(self,txt):#sepatramos en una lista las palabras
		"""print(txt)"""
		words=txt
		list_word=txt.split()
		return(list_word)

	def contWord(self,words):
		w=words
		l_w=self.txtSeparator(w)#llamamos a txtSeparator
		list_ranking=[]#lista de palabras repetidas y num repeticiones
		ranking=[]#10 palabras mas repetidas
		find_w=[]#palabra encontrada y num de veces
		cont=""#guardaremos el texto omitiendo las repetidas
		"""En este for vamos a recorer el listado del texto(l_w)   """
		for i in range(len(l_w)):
			if len(list_ranking)>0:#si ya ha y dato en la list_ranking
				dobles=re.findall(l_w[i] ,cont)#buscamos la palabra 
				#en cont(texto no repetido)
				if len(dobles)>0:#si esta repetido no hacemos nada
					dobles=0
				else:#si no esta repetido
					cont=cont+" "+l_w[i]#añadimos la palabra al texto de no repetidos
					encontradas=re.findall(l_w[i] ,w)#buscamos la palabra e el texto original
					tot_encont=int(len(encontradas))#total coincidencias
					find_w=l_w[i],tot_encont#añadimos la palabra y las coincidencias a find_w
					list_ranking.append(find_w)#añadimos a la lista la variable find_w
					list_ranking=sorted(list_ranking, key=lambda item: (item[1]), reverse=True)
					#ordemamos la lista de ranking

			else:#si aun no hay palabra y coincidencias en la lista(list_ranking)
				cont=cont+" "+l_w[i]#añadimos palabra no coicidente al texto chivato
				encontradas=re.findall(l_w[i] ,w)#buscamos la palabra en el texto original
				tot_encont=int(len(encontradas))
				if encontradas[0]==l_w[i]:#si se encuantra la palabra en texto original
					find_w=l_w[i],tot_encont#agrupamos palabra y coincidencias en la variable
					list_ranking.append(find_w)#añadimos la variable a la lista 
					list_ranking=sorted(list_ranking, key=lambda item: (item[1]), reverse=True)
		for i in range(len(list_ranking)):#con este for sacamos las 10 mejores
			if i<10:
				ranking.append(list_ranking[i])
		#print(cont)
		#print(find_w)
		return(ranking)
		

	def mostrar():
		return(txtAnalizar)
txt=rankingText()

