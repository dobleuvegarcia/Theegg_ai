class InvertirPalabras():

	def PedirDatos(self):
		self.num=int(input("introduce un numero de casos a invertir:  "))
		self.frases=[]
		for i in range(self.num):
	 		f=input("introduce frase a invertir:  ")
	 		self.frases.append(f)
		return(self.frases)

	def InvertirFrases(self):
		f_invertir=[]
		for n in range(len(self.frases)):#en el rango de todas las frases introducidas
			separador=[]
			n_frase=self.frases[n]
			palabra=""
			terminado=len(n_frase)-1
			for p in  range(len(n_frase)):#recorremos la frase
				palabra+=n_frase[p] #guardamos la palabras
				if n_frase[p]==" " or p==terminado: #separadas por espacios o hasta que la frase termina
					separador.append(palabra)#añadimos las palabras de una frase
					palabra=""
			separador.reverse()#invertimos la frase
			f_invertir.append(separador)#añadimos frases invertidas
		return(f_invertir)#retornamos conjunto frases invertidas

	def Mostrar(self,f):
		#en este metodo recoremos las palabras invertidas de una frase 
		self.f=f
		palabras=""
		for i in range(len(self.f)):
			palabras+=self.f[i]+" "
		return(palabras)#devolvemos la frase con las palabras invertidas



arr_frases=InvertirPalabras()
arr_frases.PedirDatos()
invertir=arr_frases.InvertirFrases()
for i in range(len(invertir)):#por cada frase invertida
	f=invertir[i]
	pantalla=arr_frases.Mostrar(f)#mostramos en pantalla la frase de i
	print("CASE #", i,": ", pantalla)
