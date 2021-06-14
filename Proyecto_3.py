from tkinter import *
import tkinter as tk
from tkinter import messagebox


def ventanaPrincipal():
    pantalla = tk.Tk()
    pantalla.geometry("600x300")
    pantalla.title("El Gran Torneo")
    pantalla.config(bg = "#0000A0")
    
    etiquetaNombre=tk.Label(pantalla,bg = "#0000A0",text="Nombre completo:",font=("Modern No. 20","12"))
    etiquetaNombre.place(x=300,y=20)
    
    entrada1 = tk.Entry(pantalla,text="",font=("Modern No. 20","12"))
    entrada1.place(x=300,y=50)

    etiquetaUsuario=tk.Label(pantalla,bg = "#0000A0",text="Nombre de usuario:",font=("Modern No. 20","12"))
    etiquetaUsuario.place(x=300,y=100)
    
    entrada2 = tk.Entry(pantalla, text="",font=("Modern No. 20","12"))
    entrada2.place(x=300,y=130)

    etiquetaContraseña=tk.Label(pantalla,bg = "#0000A0",text="Contraseña:",font=("Modern No. 20","12"))
    etiquetaContraseña.place(x=300,y=180)
    
    entrada3 = tk.Entry(pantalla, text="",font=("Modern No. 20","12"))
    entrada3.place(x=300,y=210)

    boton = tk.Button(pantalla,text = "Ingresar",font=("Times new roman","12"),
                      command = lambda: controlAcceso(Nombre.get(),Usuario.get(),Contraseña.get()))
    boton.place(x=200,y=200)

    def controlAcceso(Nombre,Usuario,Contraseña):
        Nombre= entrada1.get()
        Usuario = entrada2.get()
        Contraseña = entrada3.get()
        Archivo = open("control de acceso.txt")
        Leer = Archivo.readlines()
        if("Nombre completo:"+Nombre+"\n") in Leer:
            if("Nombre de usuario:"+Usuario+"\n") in Leer:
                if 
        
        Modificar3(Nombre,Direccion,Provincia,Señas,leer,indice)
        Modificar.destroy()



#Nomnbre: leer_archivo_claves
#Entradas: No recibe
#Salidas: verificar si se encuentra la clave en un archivo.txt
#Restricciones: No recibe

def leer_archivo_claves():
    archivo_claves = open("Usuarios.txt")
    lineas = archivo_claves.readlines()
    archivo_claves.close()
    lineas_modificadas = []
    for linea in lineas:
        linea = linea.replace("\n","")
        lineas_modificadas += [linea]
    return lineas_modificadas

#def definicionPersonajes(pantalla):







ventanaPrincipal()
