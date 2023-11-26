from app2 import semen
from pytube import YouTube
from tkinter import *
from tkinter import messagebox as MessageBox

#funcion que inicia la descarga del video
#que inicializa la variable "boton"
def accion():
    enlace=videos.get()
    video = YouTube(enlace)
    descargar = video.streams.get_highest_resolution()
    descargar.download()

#funcion que mustra la segunda ventana al ser
#inicializada por la variable "helpmenu"
def popup():
    semen()
    #MessageBox.showinfo("sobre mi","https://xnxx.com")


#se crea una ventanita
root = Tk()

#le damos un borde
root.config(bd=15)

#y le ponemos un titulo a la ventanita
root.title("descargador")

#definimos una variable que agarrara
#un logo para la ventanita
imagen = PhotoImage(file="hacker2.png")

#recoge el logo del programa de la variable "imagen"
foto = Label(root, image=imagen, bd=0)

#le decimos donde se posisionara la imagen
#dentro de la ventanita
foto.grid(row=0, column=0)

#VENTANAS EMERGENTES
#
#
menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

#Boton "Informacion" que contiene dentro de ella#
#la variable "helpmenu" y que aparece al llamar a 
#la funcion "popup" solo cuando se hace click
menubar.add_cascade(label="mirar", menu=helpmenu)
helpmenu.add_command(label="descargado", command=popup)

#boton que para el funcionamiento de todo el programa#
menubar.add_command(label="Cerrar", command=root.destroy)

#variable que contiene y muestra el texto en cuestion#
instruccion = Label(root, text="Programa beta 1\n")
#ubicacion del texto#
instruccion.grid(row=0, column=1)


####descargar el video ####
#input donde se ingresara la url#
videos = Entry(root)
videos.grid(row=1, column=1)

#boton que llama a la funcion "accion"
#ejecutando asi la descarga del video por medio de 
#la url
boton = Button(root, text="Descargar", command=accion)
boton.grid(row=2, column=1)


root.mainloop()
