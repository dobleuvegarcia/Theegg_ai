try:
#guardo en la variable num_usu el decimal introducido por el usuario
	num_usu=float(input("introduce un numero decimal entre 0.0001 y 0.9999 acuerdate de introducir el punto no la coma."))
	if num_usu>0.9999 or num_usu<0.0001:#cotejo k este entre 0.9999 y 0.0001
		num_usu=float(input("introduce un numero decimal entre 0.0001 y 0.9999 acuerdate de introducir el punto no la coma."))
	else:
		num_usu=int(num_usu*10000)#convierto a entero el numero decimal
		i=2
		denominador=10000
		for i in range(2,num_usu):#recorro los numeros divisibles hasta el numero usuario
			while denominador%i==0 and num_usu%i==0: #mientras si los dos son divisibles divido tantas veces sea necesario
				num_usu=num_usu/i
				denominador=denominador/i
		num_usu=int(num_usu)#convierto a entero num_usu y denominador no se porque me expresaba al imprimir por pantalla hexadecimal 
		denominador=int(denominador)
		print("la fracion irreducible es:  " + str(num_usu) + "/" + str(denominador))
except:
	print(" fallo has introducido una coma o string asi que fin del programa vuelve a ejecutarlo tu mismo")
		
