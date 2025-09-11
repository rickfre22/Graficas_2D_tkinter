from tkinter import *
import random
#variables globales
BASE = 460
ALTURA = 220

# ventana pricipal
ventana_principal = Tk()
ventana_principal.title("Graficas 2D")
ventana_principal.resizable(False,False)
ventana_principal.geometry("500x500")
ventana_principal.config(bg="white")



# Frame de graficación
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="green",width=480,height=240)
frame_graficacion.place(x=10,y=10)

#lienzo de graficacion
c =Canvas(frame_graficacion,width=BASE,height=ALTURA)
c.config(bg="black")
c.place(x=10,y=10)

#Figuras de color y tamaño aleatorio
for i in range(100):
    x = random.randint(0,BASE-20)
    y = random.randint(0,ALTURA - 20)

    color = "#"

    for caracter in range(6):
        color =color +random.choice("01123456789ABCDEF")

    ciculo = c.create_oval(x,y,x+20,y+20,fill=color)



#frame de controles
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="black",width=480,height=230)
frame_controles.place(x=10,y=260)

#desplegar ventana pricipal
ventana_principal.mainloop()