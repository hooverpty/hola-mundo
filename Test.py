# Notas sobre la libreria Tkinter de Python para la generacion de interfases graficas.#
# Ing. Haim Martinez
# jhaim04@gmail.com


import tkinter # Esta es la libreria que estoy utilizando para realizar las interfaces graficas.
from tkinter import * #Importamos todos los widgets que tkinter tiene para generar las interfaces graficas.

#Declaracion de la ventana de logueo
ventana = tkinter.Tk()
#ventana.attributes("-alpha", 0.8) #con este comando hago que la ventana sea transparente y el numero indicara el nivel de transparencia.
ventana.title("Haim Martinez - jhaim04@gmail.com") #titulo de la ventana
ventana.geometry("300x300+400+200") #damos tamano a la ventana y la ubicamos en la pantalla
ventana.resizable(0,0) #evitamos que el usuario modifique el tamano de la ventana

#Declaracion del Label Frame1
labelframe1 = LabelFrame(ventana, text="    Inicio de Sesion    ", padx=50, pady=40) #declaramos el labelframe1
labelframe1.pack(padx=20, pady=20) #le indicamos que muestre en pantalla el labelframe1

#Declaracion de los label de usuario y contraseña
usuario=tkinter.Label(labelframe1, text= "Usuario:")
usuario.pack()
user = tkinter.Entry(labelframe1, bd = 3)
user.pack()
contrasena=tkinter.Label(labelframe1, text = "Contrasena:")
contrasena.pack()
password = tkinter.Entry(labelframe1, bd = 3)
password.pack()


#Declaracion del los botones
b=Button(labelframe1, text="Ingresar", padx=20, pady=10)
b.pack()










################################### anotaciones ####################################################


#empiezo a declarar un label:
#etiqueta1 = tkinter.Label(ventana, text = "Etiqueta1").grid(column=0, row=0)  
#etiqueta1 = tkinter.Label(frame1, text = "Inicia sesion:")
#etiqueta1.grid(row=0, column = 3)
#etiqueta2 = tkinter.Label(frame1, text = "*****************")
#etiqueta2.pack()
#usuario = tkinter.Label(frame1, text = "Usuario: ")
#usuario.pack(side=LEFT)
#contrasena = tkinter.Label(frame1, text = "Contrasena: ")
#contrasena.pack(side=LEFT)


#frame2 = Frame(ventana, width=60,highlightbackground="red",highlightthicknes=6,bd=20)
#highlightthicknes=6 -- esto es el grueso de la linea
#highlightbackground="blue" -- esto es el color de la linea de bordea el frame
#frame2.grid(row=0,column=1,padx=20,pady=20,ipadx=80,ipady=20)


#etiqueta8 = tkinter.Label(ventana, text = "Etiqueta2").grid(column=1, row=1)
#etiqueta9 = tkinter.Label(ventana, text = "Etiqueta3").grid(column=2, row=2)
#etiqueta10 = tkinter.Label(ventana, text = "Etiqueta4").grid(column=3, row=3)


#luego para que la etiqueta salga en la ventana se debe utlizar el metodo pack
#etiqueta.pack() #sin especificar donde queremos que vaya la etiqueta

#si quisiera empezar a definir donde quiero que vaya la etiquida podria utlizar el siguiente metodo:
#etiqueta.pack(side= tkinter.BOTTOM)
#etiqueta.pack(side= tkinter.RIGHT) # con el anterior comando la etiqueta se alinea a la derecha
#etiqueta.pack(fill = tkinter.X, expand = True) #con este comando lo que hago es que la etiqueta se corra a lo largo del eje de las x
#etiqueta.pack(fill = tkinter.Y, expand = True) #con este comando lo que hago es que la etiqueta se corra a lo largo del eje de las Y
#etiqueta.pack(fill = tkinter.BOTH, expand = True) #con este comando lo que hago es rellenar todo la ventana tango en el eje de las X como en el eje de las Y

#con fill es para estirar y con side es para posicionar.

#esta es una funcion que cree para poder realizar la prueba del comando del boton en la interface grafica
#def saludo():
#    print("Hola")


#boton1 = tkinter.Button(ventana, text = "Presionar", command = saludo, padx = 40, pady =50) #de esta forma se crea un boton, hay que decirle en que ventana estara,
#el texto y con los atributos padx pady se puede escoger el tamano del boton que queremos.
#con el atributo command conecto el boton con una funcion especifica que yo le diga.
#es importante que la funcion que se le pase al boton se haga sin parentesis.

#boton1 = tkinter.Button(ventana, text = "Presionar", command = ventana.iconify, padx = 40, pady =50)
#con el comando venana.iconify lo que hace es minimizar la ventana cuando se presiona el boton

#def textodelacaja(): #esta es una funcion que se utiliza para obtener el texto de la caja de entrada y poder hacer operaciones con el.
#    text20 = cajatexto.get()
#    print(text20)
#    etiqueta["text"] = text20 # con este comando lo que hago es colocar lo que se escribe en la caja de texto y ponerlo en una etiqueta.
    
#boton1 = tkinter.Button(ventana, text = "Click", command = textodelacaja)
#boton1.pack() #con este comando le decimos que se presente en la ventana


#cajatexto = tkinter.Entry(ventana, font = "Arial 20") #con este comando se crea una caja de texto para que el usuario llene la informacion.
#con font y el numero se le indica cual sera el tipo de letra y adicional el tamano de esa letra.

#cajatexto.pack() #con esto se le indica a python que se debe colocar la caja de texto en la ventana.

#etiqueta = tkinter.Label(ventana)
#etiqueta.pack()

#con los comandos de abajo se utilizara el metodo grid
#boton1 = tkinter.Button(ventana, text = "boton1")
#oton2 = tkinter.Button(ventana, text = "boton2")
#boton3 = tkinter.Button(ventana, text = "boton3")

#boton1.grid(row = 2, column = 2)
#boton2.grid(row = 3, column = 3)

#este es un mensaje de prueba

#con este codigo se crea el mainloop para que siempre que se ejecute el codigo se corra el programa:




ventana.mainloop()



