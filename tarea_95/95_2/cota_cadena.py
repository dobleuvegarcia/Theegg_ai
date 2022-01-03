
def pedir_cadena_texto():
	text=input("introduce una cadena de texto: ")
	return(text)
def cota_texto(text):
	longitud=len(text)
	if longitud>=5 and longitud<10:
		print("el numero introducido es >=5 y < 10")