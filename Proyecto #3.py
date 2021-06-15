from tkinter import *
import tkinter as tk
from tkinter import messagebox

#*********************************************************************************************************************************#

class definicionDePersonajes:
    def __init__(self):
        self.Tipo = []
        self.Sexo = []
        self.NombreCompleto = []
        self.AlterEgo = []
        self.caracteristicas = []

    def agregarCaracteristicas(self,velocidad,fuerza,inteligencia,defensa,magia,telepatia,
                               estrategia,volar,elasticidad,regeneracion):
        
        self.caracteristicas += [[velocidad,fuerza,inteligencia,defensa,magia,telepatia,
                                  estrategia,volar,elasticidad,regeneracion]]

#*********************************************************************************************************************************#
def ventanaPrincipal():
    pantalla = tk.Tk()
    pantalla.geometry("600x300")
    pantalla.title("El Gran Torneo")
    pantalla.config(bg = "orange")
    
    etiquetaNombre=tk.Label(pantalla,bg = "orange",text="Nombre completo:",font=("Modern No. 20","12"))
    etiquetaNombre.place(x=40,y=20)
    
    entrada1 = tk.Entry(pantalla,text="",font=("Modern No. 20","12"))
    entrada1.place(x=40,y=50)

    etiquetaUsuario=tk.Label(pantalla,bg = "orange",text="Nombre de usuario:",font=("Modern No. 20","12"))
    etiquetaUsuario.place(x=40,y=100)
    
    entrada2 = tk.Entry(pantalla, text="",font=("Modern No. 20","12"))
    entrada2.place(x=40,y=130)

    etiquetaContraseña=tk.Label(pantalla,bg = "orange",text="Contraseña:",font=("Modern No. 20","12"))
    etiquetaContraseña.place(x=40,y=180)
    
    entrada3 = tk.Entry(pantalla, text="",font=("Modern No. 20","12"))
    entrada3.place(x=40,y=210)

    boton = tk.Button(pantalla,text = "Ingresar",font=("Times new roman","12"),
                      command = lambda:
                      control_acceso(entrada1.get(),entrada2.get(),entrada3.get()))
    boton.place(x=300,y=130)

    boton2 = tk.Button(pantalla,text = "Añadir Usuario",font=("Times new roman","12"),
                      command = lambda:
                      registrar_usuario(entrada1.get(),entrada2.get(),entrada3.get()))
    boton2.place(x=400,y=130)

def control_acceso(nombre,usuario,contraseña):
     verificar = leer_archivo()
     if nombre in verificar:
          if usuario in verificar:
               if contraseña in verificar:
                    messagebox.showerror("GGG","Hola")

               else:
                    messagebox.showerror("Error","Contraseña incorrecta")
          else:
               messagebox.showerror("Error","Usuario incorrecto")
     else:
          messagebox.showerror("Error","Nombre incorrecto")

def leer_archivo():
    datos = open("Acceso.txt")
    lineas = datos.readlines()
    datos.close()
    lineas_modificadas = []
    for linea in lineas:
        linea = linea.replace("\n","")
        lineas_modificadas += [linea]
    return lineas_modificadas


def registrar_usuario(nombre,usuario,contraseña):
    almacenar_usuario = open("Acceso.txt","a")
    archivo= open("Acceso.txt")
    archivo2 = archivo.readlines()
    if (("Usuario:"+usuario + "\n") in archivo2):
            messagebox.showerror(title = "Error", message = "Ese usuario ya existe")
    else:
        almacenar_transporte = open("Acceso.txt","a")
        almacenar_transporte.write("Nombre:"+nombre +"\n")
        almacenar_transporte.write("Usuario:"+usuario+"\n")
        almacenar_transporte.write("Contraseña:"+contraseña +"\n")
        almacenar_transporte.write("************************************************"+"\n")
        almacenar_transporte.close()
        messagebox.showinfo(title = "Usuario añadido",message = "¡El usuario se ha registrado exitosamente!")

#*********************************************************************************************************************************#




ventanaPrincipal()
