#from tkinter import *
#from tkinter import messagebox as MessageBox
#import os

# def semen():
    #   root = Tk()
 #   root.config(bd=75)
  #  mensage = Label(root, text="pagina 2\n", padx=200, pady=200)
 #   mensage.grid(row=0, column=1)
    

#    menubar = Menu(root)
    #root.config(menu=menubar)
   # helpmenu = Menu(menubar, tearoff=0)

  #  menubar.add_command(label="Cerrar", command=root.destroy)

 #   root.mainloop()

#semen()


from tkinter import *
from tkinter import messagebox as MessageBox
import os

def semen():
    root = Tk()
    root.config(bd=45)

    # Directorio de las imágenes
    directorio_imagenes = "/home/kuaker/"

    # Obtener la lista de archivos en el directorio
    archivos_imagenes = [archivo for archivo in os.listdir(directorio_imagenes) if archivo.lower().endswith(('.png', '.jpg', '.jpeg'))]

    # Crear un lienzo (Canvas) y una barra de desplazamiento (Scrollbar)
    canvas = Canvas(root)
    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Crear un marco dentro del lienzo para contener las etiquetas
    frame = Frame(canvas)
    canvas.create_window((0, 0), window=frame, anchor="nw")

    # Crear etiquetas con los nombres de los archivos y mostrarlos en el marco
    for i, archivo in enumerate(archivos_imagenes):
        etiqueta = Label(frame, text=archivo)
        etiqueta.grid(row=i, column=0, padx=1, pady=1, sticky=W)

    # Configurar el evento de desplazamiento del lienzo
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    root.mainloop()

# Llamando a la función para mostrar los nombres de las imágenes con scroll
#mostrar_nombres_imagenes()

