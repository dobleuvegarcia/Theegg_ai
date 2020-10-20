from tkinter import *
from tkinter import messagebox
#from ModCodDesc import *


raiz=Tk()
raiz.iconbitmap("icono.ico")
raiz.title("*********ENIGMA*********")
raiz.config(bg="grey", bd=35, relief="groove")

raiz.resizable(False,False)




miFrame= Frame(raiz, width=500, height=400)
miFrame.config(bg="grey")

miFrame.pack()








cod=StringVar()

texto=StringVar()
textop=StringVar()
codx=StringVar()
def codificar():

	cerrar=messagebox.askokcancel("**Destruir Código**",cuadroTexto.get())

	if cerrar==True:
		raiz.destroy()
	else:
		textop=cuadroTexto.get()
		#codx=codigo(textop)
		#print(codx)

load=Label(miFrame, textvariable=cod)
load.grid(row=1, column=2)
load.config(justify="center", bg="grey", fg="#6C571B", font=("Comic Sans MS",18))




cuadroTexto=Entry(miFrame, textvariable=texto)
cuadroTexto.config(bg="#6C571B", cursor="pirate", fg="grey", font=("Comic Sans MS",18))

cuadroTexto.grid(row=3, column=2, padx="10", pady="10", columnspan=4)


#scrollVert=Scrollbar(miFrame, command=cuadroTexto.yview)
#scrollVert.grid(row=3, column=3, sticky="nsew")
#cuadroTexto.config(yscrollcommand=scrollVert.set)


nombreLabel=Label(miFrame, text="Introduce el mensaje secreto: ", bg="grey",  fg="#6C571B", font=("Comic Sans MS",18)) 
nombreLabel.grid(row=2, column=2, padx="10", pady="10")



botonCodificar=Button(raiz, text="codificar")#, command=lambda:codificar())
botonCodificar.pack()

raiz.wm_attributes("-transparentcolor", 'grey')
raiz.mainloop()