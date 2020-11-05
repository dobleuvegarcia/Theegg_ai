from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from simulador import *
#he construido una interfaz para el ejercicio 
raiz= tk.Tk()
raiz.title("*********simulador binario*********")
raiz.config(bg="#FF00FF", bd=35, relief="groove")

raiz.resizable(False,False)

miFrame= Frame(raiz, width=500, height=400)
miFrame.config(bg="#FF00FF")

miFrame.pack()


#vakido k solo introduzca numeros y el punto de la coma

def validate_entry(num):
   	 return num in "0123456789."
def binario():
	numero=float(entry.get())
	
	cerrar=messagebox.askokcancel("**PARA pasar a binario ACEPTA**",numero)
	if cerrar==True:
		convertir=Conversor(numero)
		cerrar=messagebox.askokcancel("**convertido a binario**",convertir)

	else:
		raiz.destroy()

entry = ttk.Entry(
    validate="key",
    validatecommand=(miFrame.register(validate_entry), "%S"))

entry.pack()

nombreLabel=Label(miFrame, text="introduce un numero ",bg="#FF00FF", fg="#00FFFF", font=("Comic Sans MS",18)) 
nombreLabel.grid(row=2, column=2, padx="10", pady="10")



botonCodificar=Button(miFrame, justify="center", text="convertir a binario",bg="#00FFFF", fg="#FF00FF",command=lambda:binario())
botonCodificar.grid(row=4, column=2, padx="10", pady="10")

raiz.mainloop()
