# Notas sobre la libreria Tkinter de Python para la generacion de interfases graficas.#
# Ing. Haim Martinez
# jhaim04@gmail.com

#con esto importamos la libreria y luego vamos declarando los widgets que se neceistan:
import tkinter #esta es la forma como declaramos la libreria tkinter en python3


#para declarar una ventana utilizamos el siguiente codigo:
ventana = tkinter.Tk()
ventana.attributes("-alpha", 0.8) #con este comando hago que la ventana sea transparente y el numero indicara el nivel de transparencia.
ventana.title("Incio de Sesion...")

ventana.geometry("300x300+540+200") #damos tamano a la ventana y la ubicamos en la pantalla
ventana.resizable(0,0) #evitamos que el usuario modifique el tamano de la ventana

#para empezar a utilizar widgets se utiliza el siguiente codigo:
etiqueta = tkinter.Label(ventana, text = "Hola Mundo!", bg = "gray") #bg es el color de background de la etiqueta. 
#hola

#luego para que la etiqueta salga en la ventana se debe utlizar el metodo pack
etiqueta.pack() #sin especificar donde queremos que vaya la etiqueta

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
boton1 = tkinter.Button(ventana, text = "boton1")
boton2 = tkinter.Button(ventana, text = "boton2")
boton3 = tkinter.Button(ventana, text = "boton3")

#boton1.grid(row = 2, column = 2)
#boton2.grid(row = 3, column = 3)

#este es un mensaje de prueba

#con este codigo se crea el mainloop para que siempre que se ejecute el codigo se corra el programa:
ventana.mainloop()



