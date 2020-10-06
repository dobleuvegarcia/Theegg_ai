#este pequeño programa lo he hecho para ensayar los bucles y el if para calentar motores.

#en este ejercicio valido un mail pedido por consola, solo valido que halla un arroba no tengo en cuenta el punto
#se puede hacer era por no extenderme mucho.


valido="false" #declaro valido a falso
cont=0 #declaro un contador de veces introducidas el mail
while valido=="false":
	email=input("introduce un email valido:  ") #pido por pantalla el mail a introducir
	cont=cont+1 #sumo uno a contador de emails introducidos
	minusculas_email=email.lower() #paso a minuscula el email
	captcha=0 #sumo las arrobas que hay en un email
	i=0
	for i in range(len(email)): #uso el for para recorrer el mail y ver si hay arroba y cuantas hay
		if email[i]=="@":
			valido="true" #si hay una arroba valido a true
			captcha=captcha+1 #sumo una arroba a la variable captcha
			if captcha>1: # si hay mas de una arroba 
				valido="false" #valido lo vuelvo a poner en falso
	print(f"has tecleado {captcha} @")
	print("Has introducido " + str(cont) + " intentos  ")#paso a string la variable cont para poder mostrarla por pantalla
if valido=="true": #si solo hay una arroba introduciomos mail validandolo.
	print("correcto agregando " + minusculas_email + " A LA BASE DATOS")
