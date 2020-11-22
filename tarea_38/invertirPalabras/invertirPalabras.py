class InvertirParametrosDeValores():

	def __init__(self):
		self.valores=int(input("Cantidad de valores a analizar :  "))
		self.params_valor=[]#parametros por valor
		for i in range(self.valores):#por cada rango de valores
	 		f=input("parametros a invertir, valor N "+(str(i+1))+" :  ")
	 		self.params_valor.append(f)#añadimos los parametros por cada valor

	def InvertirParametros(self):
		params_invertir=[]
		for n in range(len(self.params_valor)):#en el rango de todos las valores introducidos
			conj_params=[]
			parametro=""
			f_arch=len(self.params_valor[n])-1#variable fin_archivo de los parametros por valor
			for p in  range(len(self.params_valor[n])):#recorremos los parametros de cada valor
				parametro+=self.params_valor[n][p] #guardamos por el contenido del parametro 
				#hasta encontrar un espacio en blanco o fin de parametros por valor(fin_arch)
				if self.params_valor[n][p]==" " or p==f_arch: #separadas por espacios o hasta fin del valor
					conj_params.append(parametro)#añadimos las parametro de cada valor
					parametro=""#limpiamos contenido parametro
			conj_params.reverse()#invertimos los parametros del valor(n) 
			params_invertir.append(conj_params)#añadimos los parametros invertidos por cada valor
		return(params_invertir)#retornamos conjunto de valores con los parametros invertidas

	def Mostrar(self,f):
		#en este metodo recoremos los parametros invertidos de un valor 
		self.f=f
		parametro=""
		for i in range(len(self.f)):
			parametro+=self.f[i]+" "
		return(parametro)#devolvemos el valor con las parametro invertidas



arr_frases=InvertirParametrosDeValores()
invertir=arr_frases.InvertirParametros()
for i in range(len(invertir)):#en el rango de todos los valores
	f=invertir[i]#por cada valor invertido
	pantalla=arr_frases.Mostrar(f)#mostramos en pantalla el contenido del valor(i)
	print("CASE #", i+1,": ", pantalla)
