try:
#guardo en la variable num_usu el decimal introducido por el usuario
	num_usu=float(input("introduce un numero decimal entre 0.0001 y 0.9999 acuerdate de introducir el punto no la coma."))
	if num_usu>0.9999 or num_usu<0.0001:#cotejo k este entre 0.9999 y 0.0001

		num_usu=float(input("introduce un numero decimal entre 0.0001 y 0.9999 acuerdate de introducir el punto no la coma."))
	else:
		num_usu=int(num_usu*10000)#convierto a entero el numero decimal
		cont=0
		array_primos=[]#declaro un array para introducir los numeros primos divisibles
		i=1
		for i in range(1,num_usu):
			if num_usu % i == 0:
				array_primos.insert(cont,int(i))#inserto en el array los numeros primos divisibles de num_usuario
				cont=cont+1
	#print("los numeros primos hasta ese numero multiplicado por 10000 son : " + str(array_primos[:])) chivato de numeros primos divisibles
	i=0
	for i in array_primos:#recorro el array de numeros primos para ver si es divisible entre ambos numerador y denominador
		#print(i)
		if 10000%i==0 and num_usu%i==0:
			num_usu=num_usu/i
			denominador=10000/i
	num_usu=int(num_usu)#convierto a entero num_usu y denominador no se porque me expresava al imprimir por pantalla hexadecimal 
	denominador=int(denominador)
	print("la fracion irreducible es:  " + str(num_usu) + "/" + str(denominador))
except:
	print(" fallo has introducido una coma o string asi que fin del programa vuelve a ejecutarlo tu mismo")
