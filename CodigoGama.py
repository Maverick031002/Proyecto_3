from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import random 

#################################################################################################################################################

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
    def __init__(self,NombreTorneo,Fecha,LugarTorneo,NumeroLuchas,Luchas):
        self.NombreTorneo = NombreTorneo
        self.Fecha = Fecha
        self.LugarTorneo = LugarTorneo
        self.NúmeroLuchas = NumeroLuchas
        self.Luchas = Luchas
        
       # self.BandoGanador = BandoGanador

class definicionDeLuchas:
    def __init__(self,NombreHeroe1,NombreHeroe2,Ganador1,Ganador2,Ganador3,Winner):
        self.NombreHeroe1 = NombreHeroe1
        self.NombreHeroe2 = NombreHeroe2
        self.Ganador1 = Ganador1
        self.Ganador2 = Ganador2
        self.Ganador3 = Ganador3
        self.Winner = Winner

class General:
    def __init__(self):
        self.torneo = []
        self.personaje = []
        self.luchas = []
        
#################################################################################################################################################
    def menuPrincipal(self):
        pantalla = tk.Tk()
        pantalla.geometry("600x300")
        pantalla.title("El Gran Torneo")
        pantalla.config(bg = "orange")

        def crear_borrar_character():
            G.crear_borrar_character()
        boton1 = tk.Button(pantalla,text = "Nuevo Character",font=("Times new roman","12"),bg = ("#F57F17"),
                          command =crear_borrar_character)
        boton1.place(x=100,y=60)

        def crear_borrar_torneo():
            G.crear_borrar_torneo()
        boton2 = tk.Button(pantalla,text = "Nuevo Torneo",font=("Times new roman","12"),bg = ("#F57F17"),
                          command =crear_borrar_torneo)
        boton2.place(x=400,y=60)

        #def estadisticas():
        
        boton3 = tk.Button(pantalla,text = "Estadisticas",font=("Times new roman","12"),bg = ("#F57F17"))
        boton3.place(x=266,y=20)

        #def start():
    
        boton4 = tk.Button(pantalla,text = "START",font=("Times new roman","12"),bg = ("#F57F17"))
        boton4.place(x=277,y=100)

        boton5 = tk.Button(pantalla,text = "Salir",font=("Times new roman","12"),bg = ("#F57F17"),
                          command = pantalla.destroy)
        boton5.place(x=285,y=180)

        
    def ventanaPrincipal(self):
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
        def Acceso():
            G.control_acceso(entrada1.get(),entrada2.get(),entrada3.get())
        boton = tk.Button(pantalla,text = "Ingresar",font=("Times new roman","12"),
                          command =Acceso )
        boton.place(x=300,y=130)
        def Registar():
            G.registrar_usuario(entrada1.get(),entrada2.get(),entrada3.get())
        boton2 = tk.Button(pantalla,text = "Añadir Usuario",font=("Times new roman","12"),
                          command =Registar )
        boton2.place(x=400,y=130)

    def control_acceso(self,nombre,usuario,contraseña):
         archivo=open("Acceso.txt")
         Verificar=archivo.readlines()
         if("Nombre:"+nombre+"\n")in Verificar:
             indice=Verificar.index("Nombre:"+nombre+"\n")
             if "Usuario:"+usuario+"\n" in Verificar[indice+1]:
                 if "Contraseña:"+contraseña+"\n" in Verificar[indice+2]:
                     G.menuPrincipal()
                 else:
                     messagebox.showerror("Error","Contraseña incorrecta")
             else:
                  messagebox.showerror("Error","Usuario incorrecto")
         else:
              messagebox.showerror("Error","Nombre incorrecto")

    def registrar_usuario(self,nombre,usuario,contraseña):
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

#################################################################################################################################################

    def crear_borrar_character(self):
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

        etiquetaElasticidad=tk.Label(pantalla,bg = "orange",text="Elasticidad:",font=("Modern No. 20","12"))
        etiquetaElasticidad.place(x=360,y=260)

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

        def Validar():
            G.validar_character(entrada1.get(),entrada2.get(),entrada3.get(),
                                           entrada4.get(),combo1.get(),combo2.get(),combo3.get(),combo4.get(),combo5.get(),combo6.get(),
                                           combo7.get(),combo8.get(),combo9.get(),combo10.get())

        boton = tk.Button(pantalla,text = "Agregar",font=("Times new roman","12"),
                         command = Validar)
                    
        boton.place(x=700,y=130)
        
        def eliminar():
            G.eliminar_character()
        boton2 = tk.Button(pantalla,text = "Eliminar",font=("Times new roman","12"),
                         command = eliminar)
        boton2.place(x=800,y=130)

         

    def validar_character(self,tipo,genero,nombre,alterEgo,velocidad,fuerza,inteligencia,defensa,magia,telepatia,estratega,elasticidad,volar,regeneracion):
        velocidad = int(velocidad)
        fuerza = int(fuerza)
        inteligencia = int(inteligencia)
        defensa = int(defensa)
        magia = int(magia)
        telepatia = int(telepatia)
        estratega = int(estratega)
        elasticidad = int(elasticidad)
        volar = int(volar)
        regeneracion = int(regeneracion)

        suma = (velocidad+fuerza+inteligencia+defensa+magia+telepatia+estratega+elasticidad+volar+regeneracion)

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
            luchadores.write("Elasticidad:"+str(elasticidad) +"\n")
            luchadores.write("Volar:"+str(volar) +"\n")
            luchadores.write("Regeneracion:"+str(regeneracion) +"\n")
            luchadores.write("-------------------------------------"+"\n")
            luchadores.close()
            messagebox.showinfo(title = "Luchador añadido",message = "¡El Luchador se ha registrado exitosamente!")
            
#################################################################################################################################################

    #Nomnbre: eliminar_empresa
    #Entradas: No recibe
    #Salidas: Generar un menu de eliminar empresa
    #Restricciones: No recibe
            
    def eliminar_character(self):
        window = tk.Tk()
        window.geometry("600x300")
        window.config(bg = "orange")
        window.title("Eliminando Personaje")
        
        etiqueta1 = tk.Label(window, text = "Alter Ego a eliminar").pack()
        AlterEgo = tk.Entry(window,text = "", font=("Times new roman","12"), bg="white", fg="Black")
        AlterEgo.pack()

    #Pasa los datos a la siguiente funcion
        def eliminar_luchador():
            variable = AlterEgo.get()
            G.eliminar_luchador2(variable)
        
        tk.Button(window,text="Eliminar",font = ("Times new roman","12"),bg="#e7c4e5",fg="Black",
                  command =  eliminar_luchador).pack()
        
        window.mainloop()

    #Verifica si la cedula de la empresa que va a eliminar esta en el archivo
    def eliminar_luchador2(self,alterEgo):
        open_file = open("Luchadores.txt")
        luchadores = open_file.readlines()
        if (("Alter Ego:"+alterEgo+"\n")in luchadores):
            alterEgo=str(alterEgo)
            potencia = luchadores.index("Alter Ego:"+alterEgo+"\n")
            alterEgo = G.deleteLuchador(luchadores, potencia-3, 0)
            open_file.close()
            open_file = open("Luchadores.txt", "w")
            print(alterEgo)
            open_file.write(alterEgo)
            open_file.close()
            messagebox.showinfo(title = "Exito", message = "Luchador eliminado exitosamente")
                
        else:
            messagebox.showerror(title = "Error", message = "Luchador inexistente")
            
        #elimina las lineas 
    def deleteLuchador(self,delete,ContarLineas,contador):
        cont=0
        while cont!=15:
            delete.pop(ContarLineas)
            cont+=1

        return G.TransformarSTR(delete)
                 

    #Nombre: TransformarSTR
    #Entradas: un parámetro llamado delete
    #Salidas: transformar el parámetro a una lista
    #Restricciones: el parámetro debe ser una lista
        
    def TransformarSTR(self,delete):
        if isinstance(delete,list):
            STR = ""
            for indice in delete:
                STR += indice
            return STR
        else:
            print("")
            
#################################################################################################################################################

    def crear_borrar_torneo(self):
        pantalla = tk.Tk()
        pantalla.geometry("500x300")
        pantalla.title("El Gran Torneo")
        pantalla.config(bg = "orange")
        cont = []

        for num in range (0,6):
            cont += [num]

        etiquetaNumeroLuchas=tk.Label(pantalla,bg = "orange",text="Numero de luchas:",font=("Modern No. 20","12"))
        etiquetaNumeroLuchas.place(x=40,y=20)
        entrada1 = ttk.Combobox(pantalla)
        entrada1['values'] = cont
        entrada1.place(x=40,y=50)
         
        etiquetaNombre=tk.Label(pantalla,bg = "orange",text="Nombre del Torneo:",font=("Modern No. 20","12"))
        etiquetaNombre.place(x=40,y=80)
        entrada2 = tk.Entry(pantalla, text="",font=("Modern No. 20","12"))
        entrada2.place(x=40,y=110)

        etiquetaLugar=tk.Label(pantalla,bg = "orange",text="Lugar del Torneo:",font=("Modern No. 20","12"))
        etiquetaLugar.place(x=40,y=140)
        entrada3 = tk.Entry(pantalla, text="",font=("Modern No. 20","12"))
        entrada3.place(x=40,y=170)

        etiquetaFecha=tk.Label(pantalla,bg = "orange",text="Fecha:",font=("Modern No. 20","12"))
        etiquetaFecha.place(x=40,y=200)
        entrada4 = tk.Entry(pantalla, text="",font=("Modern No. 20","12"))
        entrada4.place(x=40,y=230)
        
        def Manual():
            G.manual(entrada1.get(),entrada2.get(),entrada3.get(),entrada4.get())
        boton = tk.Button(pantalla,text = "Manual",font=("Times new roman","12"),
                         command = Manual)
        boton.place(x=343,y=75)
        
        def Persona_vs_Programa():
             G.persona_vs_programa(entrada1.get(),entrada2.get(),entrada3.get(),entrada4.get())
        boton2 = tk.Button(pantalla,text = "Persona vs Programa",font=("Times new roman","12"),
                         command = Persona_vs_Programa)
        boton2.place(x=300,y=135)

        def Programa_vs_Programa():
            G.programa_vs_programa(entrada1.get(),entrada2.get(),entrada3.get(),entrada4.get(),combo1.get())
        boton3 = tk.Button(pantalla,text = "Programa vs Programa",font=("Times new roman","12"),
                         command = Programa_vs_Programa)
        boton3.place(x=296,y=195)

    def manual(self,luchas,nombre,lugar,fecha):
        pantalla = tk.Tk()
        pantalla.geometry("500x300")
        pantalla.title("El Gran Torneo")
        pantalla.config(bg = "orange")
        abrir = open("Luchadores.txt")
        abrir2 = abrir.readlines()
        cont = 0
        datos = []

        etiquetaPlayer1=tk.Label(pantalla,bg = "orange",text="Player 1:",font=("Modern No. 20","12"))
        etiquetaPlayer1.place(x=40,y=20)
        
        etiquetaPlayer2=tk.Label(pantalla,bg = "orange",text="Player 2:",font=("Modern No. 20","12"))
        etiquetaPlayer2.place(x=300,y=20)
        
        for file in abrir2:
            if cont == 3:
                datos += [file]
                cont += 1
            elif cont == 14:
                cont = 0
            else:
                cont += 1
        else:
            if int(luchas) >= 1:
                entrada1 = ttk.Combobox(pantalla)
                entrada1['values'] = datos
                entrada1.place(x=40,y=50)
                cont += 1

                entrada6 = ttk.Combobox(pantalla)
                entrada6['values'] = datos
                entrada6.place(x=300,y=50)
                cont += 1

                if int(luchas) >= 2:
                    entrada2 = ttk.Combobox(pantalla)
                    entrada2['values'] = datos
                    entrada2.place(x=40,y=80)
                    cont += 1

                    entrada7 = ttk.Combobox(pantalla)
                    entrada7['values'] = datos
                    entrada7.place(x=300,y=80)
                    cont += 1
                
                    if int (luchas) >= 3:    
                        entrada3 = ttk.Combobox(pantalla)
                        entrada3['values'] = datos
                        entrada3.place(x=40,y=110)
                        cont += 1

                        entrada8 = ttk.Combobox(pantalla)
                        entrada8['values'] = datos
                        entrada8.place(x=300,y=110)
                        cont += 1

                        if int(luchas) >= 4:
                            entrada4 = ttk.Combobox(pantalla)
                            entrada4['values'] = datos
                            entrada4.place(x=40,y=140)
                            cont += 1

                            entrada9 = ttk.Combobox(pantalla)
                            entrada9['values'] = datos
                            entrada9.place(x=300,y=140)
                            cont += 1

                            
                            if int(luchas) >= 5:
                                entrada5 = ttk.Combobox(pantalla)
                                entrada5['values'] = datos
                                entrada5.place(x=40,y=170)
                                cont += 1
        
                                entrada10 = ttk.Combobox(pantalla)
                                entrada10['values'] = datos
                                entrada10.place(x=300,y=170)
                                cont += 1

        def validarManual():
            if int((luchas)>=2):
                if int(luchas)>=3:
                    if int(luchas)>=4:
                        if int(luchas)>=5:
                            torneo1 = definiciónDeTorneo(nombre,fecha,lugar,luchas,[entrada1,entrada6,entrada2,entrada7,entrada3,
                                                                                    entrada8,entrada4,entrada9,entrada5,entrada10])
                            self.torneo(torneo1)
                        else:
                            torneo1 = definiciónDeTorneo(nombre,fecha,lugar,luchas,[entrada1,entrada6,entrada2,entrada7,entrada3,
                                                                                    entrada8,entrada4,entrada9])
                            self.torneo(torneo1)
                            G.menuPrincipal()
                            pantalla.destroy()
                    else:
                        torneo1 = definiciónDeTorneo(nombre,fecha,lugar,luchas,[entrada1,entrada6,entrada2,entrada7,entrada3,
                                                                                   entrada8])
                        self.torneo(torneo1)
                        G.menuPrincipal()
                        pantalla.destroy()
                else:
                    torneo1 = definiciónDeTorneo(nombre,fecha,lugar,luchas,[entrada1,entrada6,entrada2,entrada7])
                    self.torneo(torneo1)
                    G.menuPrincipal()
                    pantalla.destroy()
            else:
                torneo1 = definiciónDeTorneo(nombre,fecha,lugar,luchas,[entrada1,entrada6])
                self.torneo(torneo1)
                G.menuPrincipal()
                pantalla.destroy()
                                           

        boton3 = tk.Button(pantalla,text = "Continuar",font=("Times new roman","12"),command = validarManual)
        boton3.place(x=296,y=195)

    def persona_vs_programa(self,luchas,nombre,lugar,fecha):
        pantalla = tk.Tk()
        pantalla.geometry("500x300")
        pantalla.title("El Gran Torneo")
        pantalla.config(bg = "orange")
        abrir = open("Luchadores.txt")
        abrir2 = abrir.readlines()
        cont = 0
        datos = []

        etiquetaPlayer1=tk.Label(pantalla,bg = "orange",text="Player 1:",font=("Modern No. 20","12"))
        etiquetaPlayer1.place(x=40,y=20)
        
        etiquetaPlayer2=tk.Label(pantalla,bg = "orange",text="Player 2:",font=("Modern No. 20","12"))
        etiquetaPlayer2.place(x=300,y=20)
        
        for file in abrir2:
            if cont == 3:
                datos += [file]
                cont += 1
            elif cont == 14:
                cont = 0
            else:
                cont += 1
        else:
            if int(luchas) >= 1:
                entrada1 = ttk.Combobox(pantalla)
                entrada1['values'] = datos
                entrada1.place(x=40,y=50)
                cont += 1

                

                if int(luchas) >= 2:
                    entrada2 = ttk.Combobox(pantalla)
                    entrada2['values'] = datos
                    entrada2.place(x=40,y=80)
                    cont += 1

                   
                
                    if int (luchas) >= 3:    
                        entrada3 = ttk.Combobox(pantalla)
                        entrada3['values'] = datos
                        entrada3.place(x=40,y=110)
                        cont += 1

                       

                        if int(luchas) >= 4:
                            entrada4 = ttk.Combobox(pantalla)
                            entrada4['values'] = datos
                            entrada4.place(x=40,y=140)
                            cont += 1

                            

                            
                            if int(luchas) >= 5:
                                entrada5 = ttk.Combobox(pantalla)
                                entrada5['values'] = datos
                                entrada5.place(x=40,y=170)
                                cont += 1
        
                               

        def validar_persona_vs_programa():
            maquina = random.saple(datos,int(luchas))
            if int((luchas)>=2):
                if int(luchas)>=3:
                    if int(luchas)>=4:
                        if int(luchas)>=5:
                            torneo1 = definiciónDeTorneo(nombre,fecha,lugar,luchas,[entrada1,maquina[0],entrada2,maquina[1],entrada3,maquina[2],
                                                                                    entrada4,maquina[3],entrada5,maquina[4]])
                            self.torneo(torneo1)
                        else:
                            torneo1 = definiciónDeTorneo(nombre,fecha,lugar,luchas,[entrada1,maquina[0],entrada2,maquina[1],entrada3,maquina[2],
                                                                                    entrada4,maquina[3]])
                            self.torneo(torneo1)
                            G.menuPrincipal()
                            pantalla.destroy()
                    else:
                        torneo1 = definiciónDeTorneo(nombre,fecha,lugar,luchas,[entrada1,maquina[0],entrada2,maquina[1],entrada3,maquina[2]])
                        self.torneo(torneo1)
                        G.menuPrincipal()
                        pantalla.destroy()
                else:
                    torneo1 = definiciónDeTorneo(nombre,fecha,lugar,luchas,[entrada1,maquina[0],entrada2,maquina[1]])
                    self.torneo(torneo1)
                    G.menuPrincipal()
                    pantalla.destroy()
            else:
                torneo1 = definiciónDeTorneo(nombre,fecha,lugar,luchas,[entrada1,maquina[0]])
                self.torneo(torneo1)
                G.menuPrincipal()
                pantalla.destroy()
                                           

        boton3 = tk.Button(pantalla,text = "Continuar",font=("Times new roman","12"),command = validar_persona_vs_programa)
        boton3.place(x=296,y=195)

    def programa_vs_programa(self,luchas,nombre,lugar,fecha):
        pantalla = tk.Tk()
        pantalla.geometry("500x300")
        pantalla.title("El Gran Torneo")
        pantalla.config(bg = "orange")
        abrir = open("Luchadores.txt")
        abrir2 = abrir.readlines()
        cont = 0
        datos = []

        etiquetaPlayer1=tk.Label(pantalla,bg = "orange",text="Player 1:",font=("Modern No. 20","12"))
        etiquetaPlayer1.place(x=40,y=20)
        
        etiquetaPlayer2=tk.Label(pantalla,bg = "orange",text="Player 2:",font=("Modern No. 20","12"))
        etiquetaPlayer2.place(x=300,y=20)
        
        for file in abrir2:
            if cont == 3:
                datos += [file]
                cont += 1
            elif cont == 14:
                cont = 0
            else:
                cont += 1
                        

        def validar_programa_vs_programa():
            maquina = random.saple(datos,int(luchas)*2)
            if int((luchas)>=2):
                if int(luchas)>=3:
                    if int(luchas)>=4:
                        if int(luchas)>=5:
                            torneo1 = definiciónDeTorneo(nombre,fecha,lugar,luchas,maquina)
                            self.torneo(torneo1)
                        else:
                            torneo1 = definiciónDeTorneo(nombre,fecha,lugar,luchas,maquina)
                            self.torneo(torneo1)
                            G.menuPrincipal()
                            pantalla.destroy()
                    else:
                        torneo1 = definiciónDeTorneo(nombre,fecha,lugar,luchas,maquina)
                        self.torneo(torneo1)
                        G.menuPrincipal()
                        pantalla.destroy()
                else:
                    torneo1 = definiciónDeTorneo(nombre,fecha,lugar,luchas,maquina)
                    self.torneo(torneo1)
                    G.menuPrincipal()
                    pantalla.destroy()
            else:
                torneo1 = definiciónDeTorneo(nombre,fecha,lugar,luchas,maquina)
                self.torneo(torneo1)
                G.menuPrincipal()
                pantalla.destroy()
                                           

        boton3 = tk.Button(pantalla,text = "Continuar",font=("Times new roman","12"),command = validar_programa_vs_programa)
        boton3.place(x=296,y=195)




G = General()
G.menuPrincipal()
