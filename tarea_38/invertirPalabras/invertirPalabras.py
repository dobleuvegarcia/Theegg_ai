class InvertirPalabras():

	def __init__(self):
		pass
		
	def PedirDatos(self):
		self.num=int(input("introduce un numero de casos a invertir:  "))
		self.frases=[]
		for i in range(self.num):
	 		f=input("introduce frase a invertir:  ")
	 		self.frases.append(f)
		return(self.frases)

	def InvertirFrases(self):
		separador=[]
		f_invertir=[]
		for n in range(len(self.frases)):
			separador=[]
			n_frase=self.frases[n]
			palabra=""
			terminado=len(n_frase)-1
			for p in  range(len(n_frase)):
				palabra+=n_frase[p]
				if n_frase[p]==" " or p==terminado:
					separador.append(palabra)
					palabra=""
			separador.reverse()
			f_invertir.append(separador)	
		return(f_invertir)

	def Mostrar(self,f):
		self.f=f
		palabras=""
		for i in range(len(self.f)):
			palabras+=self.f[i]+" "
		return(palabras)



arr_frases=InvertirPalabras()
arr_frases.PedirDatos()
invertir=arr_frases.InvertirFrases()
for i in range(len(invertir)):
	f=invertir[i]
	pantalla=arr_frases.Mostrar(f)
	print("CASE #", i,": ", pantalla)
