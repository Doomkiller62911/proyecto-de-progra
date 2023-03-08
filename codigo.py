import tkinter

ventana = tkinter.Tk()
ventana.geometry("400x300")

def saludo():
    print("hola como estas")

boton1 = tkinter.Button(ventana , text = "Presiona", command= saludo, bg= "yellow", fg= "blue", relief= "flat" )
etiqueta = tkinter.Label(ventana, text = "CINEPOLIS", font= "Times 15 bold",bg= "#00ffff", fg= "#000000", bd= "5"  )
etiqueta.pack(side= "top", fill= tkinter.X, expand= True)
boton1.pack(side="bottom")

ventana.mainloop()
