from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

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

class definiciónDeTorneo:
    def __init__(self,NombreTorneo,Fecha,LugarTorneo,NumeroLuchas,Luchas,BandoGanador):
        self.NombreTorneo = NombreTorneo
        self.Fecha = Fecha
        self.LugarTorneo = LugarTorneo
        self.NúmeroLuchas = NumeroLuchas
        self.Luchas = Luchas
        self.BandoGanador = BandoGanador

class definicionDeLuchas:
    def __init__(self,NombreHeroe1,NombreHeroe2,Ganador1,Ganador2,Ganador3,Winner):
        self.NombreHeroe1 = NombreHeroe1
        self.NombreHeroe2 = NombreHeroe2
        self.Ganador1 = Ganador1
        self.Ganador2 = Ganador2
        self.Ganador3 = Ganador3
        self.Winner = Winner

        
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
                    crear_borrar_character()

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

def crear_borrar_character():
    pantalla = tk.Tk()
    pantalla.geometry("1200x600")
    pantalla.title("El Gran Torneo")
    pantalla.config(bg = "orange")
    cont = []

    for num in range (0,100):
        cont += [num]

     
    etiquetaTipo=tk.Label(pantalla,bg = "orange",text="Tipo:",font=("Modern No. 20","12"))
    etiquetaTipo.place(x=40,y=20)
     
    entrada1 = ttk.Combobox(pantalla)
    entrada1['values'] = ("Heroe","Villano")
    entrada1.place(x=40,y=50)
     
    etiquetaGenero=tk.Label(pantalla,bg = "orange",text="Género:",font=("Modern No. 20","12"))
    etiquetaGenero.place(x=200,y=20)
     
    entrada2 = ttk.Combobox(pantalla)
    entrada2['values'] = ("Hombre","Mujer")
    entrada2.place(x=200,y=50)
     
    etiquetaNombre=tk.Label(pantalla,bg = "orange",text="Nombre Completo:",font=("Modern No. 20","12"))
    etiquetaNombre.place(x=360,y=20)
    entrada3 = tk.Entry(pantalla, text="",font=("Modern No. 20","12"))
    entrada3.place(x=360,y=50)

    etiquetaAlterEgo=tk.Label(pantalla,bg = "orange",text="Nombre AlterEgo:",font=("Modern No. 20","12"))
    etiquetaAlterEgo.place(x=520,y=20)
    entrada4 = tk.Entry(pantalla, text="",font=("Modern No. 20","12"))
    entrada4.place(x=520,y=50)


    etiquetaVelocidad=tk.Label(pantalla,bg = "orange",text="Velocidad:",font=("Modern No. 20","12"))
    etiquetaVelocidad.place(x=40,y=100)

    combo1 = ttk.Combobox(pantalla)
    combo1['values'] = cont
    combo1.place(x=40,y=130)

    etiquetaFuerza=tk.Label(pantalla,bg = "orange",text="Fuerza:",font=("Modern No. 20","12"))
    etiquetaFuerza.place(x=200,y=100)

    combo2 = ttk.Combobox(pantalla)
    combo2['values'] = cont
    combo2.place(x=200,y=130)

    etiquetaInteligencia=tk.Label(pantalla,bg = "orange",text="Inteligencia:",font=("Modern No. 20","12"))
    etiquetaInteligencia.place(x=200,y=180)

    combo3 = ttk.Combobox(pantalla)
    combo3['values'] = cont
    combo3.place(x=200,y=210)

    etiquetaDefensaPersonal=tk.Label(pantalla,bg = "orange",text="Defensa Personal:",font=("Modern No. 20","12"))
    etiquetaDefensaPersonal.place(x=40,y=180)

    combo4 = ttk.Combobox(pantalla)
    combo4['values'] = cont
    combo4.place(x=40,y=210)

    etiquetaMagia=tk.Label(pantalla,bg = "orange",text="Magia:",font=("Modern No. 20","12"))
    etiquetaMagia.place(x=360,y=100)

    combo5 = ttk.Combobox(pantalla)
    combo5['values'] = cont
    combo5.place(x=360,y=130)

    etiquetaTelepatía=tk.Label(pantalla,bg = "orange",text="Telepatía:",font=("Modern No. 20","12"))
    etiquetaTelepatía.place(x=360,y=180)

    combo6 = ttk.Combobox(pantalla)
    combo6['values'] = cont
    combo6.place(x=360,y=210)

    etiquetaEstratega=tk.Label(pantalla,bg = "orange",text="Estratega:",font=("Modern No. 20","12"))
    etiquetaEstratega.place(x=40,y=260)

    combo7 = ttk.Combobox(pantalla)
    combo7['values'] = cont
    combo7.place(x=40,y=290)

    etiquetaElectricidad=tk.Label(pantalla,bg = "orange",text="Electricidad:",font=("Modern No. 20","12"))
    etiquetaElectricidad.place(x=360,y=260)

    combo8 = ttk.Combobox(pantalla)
    combo8['values'] = cont
    combo8.place(x=360,y=290)

    etiquetaVolar=tk.Label(pantalla,bg = "orange",text="Volar:",font=("Modern No. 20","12"))
    etiquetaVolar.place(x=520,y=100)

    combo9 = ttk.Combobox(pantalla)
    combo9['values'] = cont
    combo9.place(x=520,y=130)

    etiquetaRegeneracion=tk.Label(pantalla,bg = "orange",text="Regeneración:",font=("Modern No. 20","12"))
    etiquetaRegeneracion.place(x=200,y=260)

    combo10 = ttk.Combobox(pantalla)
    combo10['values'] = cont
    combo10.place(x=200,y=290)
    


    boton = tk.Button(pantalla,text = "Agregar",font=("Times new roman","12"),
                     command = lambda:
                     validar(entrada1.get(),entrada2.get(),entrada3.get(),entrada4.get(),combo1.get(),combo2.get(),combo3.get(),combo4.get(),combo5.get(),combo6.get(),
                                       combo7.get(),combo8.get(),combo9.get(),combo10.get()))
    boton.place(x=700,y=130)
     
    boton2 = tk.Button(pantalla,text = "Eliminar",font=("Times new roman","12"),
                     command = lambda:
                     registrar_usuario(entrada1.get(),entrada2.get(),entrada3.get(),entrada4.get(),combo1.get(),combo2.get(),combo3.get(),combo4.get(),combo5.get(),combo6.get(),
                                       combo7.get(),combo8.get(),combo9.get(),combo10.get()))
    boton2.place(x=800,y=130)

     

def validar(tipo,genero,nombre,alterEgo,velocidad,fuerza,inteligencia,defensa,magia,telepatia,estratega,electricidad,volar,regeneracion):
    velocidad = int(velocidad)
    fuerza = int(fuerza)
    inteligencia = int(inteligencia)
    defensa = int(defensa)
    magia = int(magia)
    telepatia = int(telepatia)
    estratega = int(estratega)
    electricidad = int(electricidad)
    volar = int(volar)
    regeneracion = int(regeneracion)
    
    suma = (velocidad+fuerza+inteligencia+defensa+magia+telepatia+estratega+electricidad+volar+regeneracion)

    if suma != 100:
        messagebox.showerror("Error","Los poderes deben sumar 100 de poder")
        
    else:
        luchadores = open("Luchadores.txt","a")
        luchadores.write("Tipo:"+tipo +"\n")
        luchadores.write("Genero:"+genero+"\n")
        luchadores.write("Nombre:"+nombre +"\n")
        luchadores.write("Alter Ego:"+alterEgo +"\n")
        luchadores.write("Velocidad:"+str(velocidad)+"\n")
        luchadores.write("Fuerza:"+str(fuerza) +"\n")
        luchadores.write("Inteligencia:"+str(inteligencia) +"\n")
        luchadores.write("Defensa:"+str(defensa) +"\n")
        luchadores.write("Magia:"+str(magia) +"\n")
        luchadores.write("Telepatia:"+str(telepatia) +"\n")
        luchadores.write("Estratega:"+str(estratega) +"\n")
        luchadores.write("Electricidad:"+str(electricidad) +"\n")
        luchadores.write("Volar:"+str(volar) +"\n")
        luchadores.write("Regeneracion:"+str(regeneracion) +"\n")
        luchadores.write("************************************************"+"\n")
        luchadores.close()
        messagebox.showinfo(title = "Luchador añadido",message = "¡El Luchador se ha registrado exitosamente!")
        
        


ventanaPrincipal()
