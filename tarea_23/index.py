#HE CREADO UNA INTERFACE DE USUARIO A LA QUE LE HE DADO UNOS EFECTOS ESPECIALES 
#de agujero y transparentes

from tkinter import *
from tkinter import messagebox 
from ModCodDesc import *
import tkinter as tk


raiz=Tk()
raiz.iconbitmap("icono.ico")
raiz.title("*********ENIGMA*********")
raiz.config(bg="grey", bd=35, relief="groove")

raiz.resizable(False,False)




enigma= Frame(raiz, width=500, height=400)
enigma.config(bg="grey")

enigma.pack()

c=[]
i=StringVar()
clav=StringVar()
clave=StringVar()
cod=StringVar()
x=StringVar()
texto=StringVar()
textop=StringVar()
codx=StringVar()
codigo=StringVar()
desco=StringVar()
clv=StringVar()
def IntroClave():
    otra_ventana = Toplevel(raiz)
    otra_ventana.title("Introducir clave")
    cText=tk.Entry(otra_ventana, textvariable=i)
    cText.config(bg="#6C571B", cursor="pirate", fg="grey", font=("Comic Sans MS",18))
    cText.grid(row=3, column=2, padx="10", pady="10", columnspan=4)
    
    botonClave=Button(otra_ventana, text="codificar", command=lambda:codificar(cText.get()))
    botonClave.grid(row=4, column=2, padx="10", pady="10")
    botonDescodificar=Button(otra_ventana, text="descodificar", command=lambda:descodificar(cText.get()))
    botonDescodificar.grid(row=4, column=4, padx="10", pady="10")
    otra_ventana.mainloop()
def codificar(x):
	clv=StringVar()
	codx=cuadroTexto.get()
	clv=str(x)
	clv=clv.upper()
	jugar=Jugada(codx, clv)
	jugar.Repetir()
	x=jugar.ObtenerLetraCodigo()
	cuadroTexto.delete(0, END)
	cuadroTexto.insert(0, x)
	
		#codx=codigo(textop)
		#print(codx)
def descodificar(x):
	codx=cuadroTexto.get()
	clvDes=str(x)
	jugar=Jugada(codx, clvDes)
	jugar.barajar(True,clvDes)
	jugar.descodificar(codx)
	jugar.RepetirPaso2()
	desco=jugar.ObtenerLetraCodigo2()
	cuadroTexto.delete(0, END)
	cuadroTexto.insert(0, desco)
		

load=Label(enigma, textvariable=cod)
load.grid(row=1, column=2)
load.config(justify="center", bg="grey", fg="#6C571B", font=("Comic Sans MS",18))




cuadroTexto=Entry(enigma, textvariable=texto)
cuadroTexto.config(bg="#6C571B", cursor="pirate", fg="grey", font=("Comic Sans MS",18))

cuadroTexto.grid(row=3, column=2, padx="10", pady="10", columnspan=4)


#scrollVert=Scrollbar(miFrame, command=cuadroTexto.yview)
#scrollVert.grid(row=3, column=3, sticky="nsew")
#cuadroTexto.config(yscrollcommand=scrollVert.set)


nombreLabel=Label(enigma, text="Introduce el mensaje secreto: ",justify="center", bg="grey",  fg="#6C571B", font=("Comic Sans MS",18)) 
nombreLabel.grid(row=2, column=2, padx="10", pady="10")



botonCodificar=Button(raiz, text="Introducir Clave", command=lambda:IntroClave())
botonCodificar.pack()

raiz.wm_attributes("-transparentcolor", 'grey')
raiz.mainloop()