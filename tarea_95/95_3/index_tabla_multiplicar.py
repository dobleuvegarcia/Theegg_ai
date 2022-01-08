import tabla_multiplicar as tm

num=tm.pedirDatos()
print(num)
for i in range(9):
	resultado=tm.tabla_multiplicar(num,i)
	print(str(num)+" * "+str(i+1)+ " = "+str(resultado))
