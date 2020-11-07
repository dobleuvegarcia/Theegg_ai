
from tkinter import ttk
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from pikachu import *
#he construido una interfaz para el ejercicio 
raiz= tk.Tk()
raiz.title("*****PIKACHU VS JIGGLYPUFF*****")

raiz.config( bg="#FF00FF",bd=35, relief="groove")

raiz.resizable(False,False)
miFrame= Frame(raiz, width=500, height=400,bg="#FF00FF")

miFrame.pack()
plf=IntVar()
jlf=IntVar()
lf=IntVar()
jugar=[]
winner=StringVar()


def vs():
	lf=Life.get()
	plf=pikLife.get()
	jlf=jilLife.get()
	jugar=Jugada(lf,plf,jlf)
	win=jugar.vs()
	for w in range(len(win)):
		winner=win[0]
		plf=win[1]
		jlf=win[2]

	
	cerrar=messagebox.askokcancel("**EL GANADOR ES**",winner)
	
	if cerrar==True:
		if plf>jlf:
			msg="el ganador es : " + str(winner)+ " con una vida de :"+ str(plf)+ " JIGGLYPUFF ha perdido con una vida de : "+str(jlf)
			cerrar=messagebox.showwarning("**PICHACHU**",msg)
		else:
			msg="el ganador es : " + str(winner)+ " con una vida de :"+ str(jlf)+ " PICHACHU ha perdido con una vida de : "+str(plf)
			cerrar=messagebox.showwarning("**JIGGLYPUFF**",msg)
	else:
		raiz.destroy()
	
		
		


img = PhotoImage(file='pikachu.png')
boton1 = Button(miFrame, text="test", width=150, height=150, image=img, justify="left",bg="#FF00FF")
boton1.grid(row=1, column=1, padx="10", pady="10")
img2 = PhotoImage(file='Jigglypuff.png')
boton2 = Button(miFrame,text="test", width=150, height=150, image=img2, justify="center",bg="#FF00FF")
boton2.grid(row=1, column=3, padx="10", pady="10")
img3 = PhotoImage(file='vs.png')
boton3 = Button(miFrame,text="test", width=150, height=150, image=img3, justify="right",bg="white",command=lambda:vs())
boton3.grid(row=1, column=2, padx="10", pady="10")

poderLabel=Label(miFrame, text="poder de Pikachu ",bg="#FF00FF", fg="#00FFFF", font=("Comic Sans MS",18)) 
poderLabel.grid(row=2, column=1, padx="10", pady="10")

pikLife=Entry(miFrame, textvariable=plf)
pikLife.config(bg="#FF00FF", cursor="pirate", fg="black", font=("Comic Sans MS",12))
pikLife.grid(row=3, column=1, padx="10", pady="10", columnspan=1)


vidaLabel=Label(miFrame, text="vida por la que convatiran ",bg="#FF00FF", fg="#00FFFF", font=("Comic Sans MS",18)) 
vidaLabel.grid(row=2, column=2, padx="10", pady="10")
Life=Entry(miFrame, textvariable=lf)
Life.config(bg="#FF00FF", cursor="pirate", fg="black", font=("Comic Sans MS",12))
Life.grid(row=3, column=2, padx="10", pady="10", columnspan=1)


poderLabel=Label(miFrame, text="poder de Jigglypuff ",bg="#FF00FF", fg="#00FFFF", font=("Comic Sans MS",18)) 
poderLabel.grid(row=2, column=3, padx="10", pady="10")
jilLife=Entry(miFrame, textvariable=jlf)
jilLife.config(bg="#FF00FF", cursor="pirate", fg="black", font=("Comic Sans MS",12))
jilLife.grid(row=3, column=3, padx="10", pady="10", columnspan=1)



raiz.mainloop()
