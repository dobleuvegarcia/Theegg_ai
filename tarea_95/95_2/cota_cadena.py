
def pedir_cadena_texto():
	text=input("introduce una cadena de texto: ")
	return(text)
def cota_texto(text):
	longitud=len(text)
	if longitud>=5 and longitud<10:
		print("El espacio de la cadena de texto introducida es  >=5 y < 10")
	else:
		print("El espacio de la cadena de texto introducida es <5 ó > 10")