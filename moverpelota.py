from tkinter import *
import random
#variables globales
BASE = 400
ALTURA = 200
RADIO = 10
desplazamiento_x = 1
desplazamiento_y = 1
intervalo = 2
centro_x =random.randint(RADIO,BASE)
centro_y = random.randint(RADIO,ALTURA)

#funciones
def mover_pelota():
    global desplazamiento_x,desplazamiento_y
    x0,y0,x1,y1 =c.coords(pelota)

    if x0 < 0 or x1 > BASE:
        desplazamiento_x = -desplazamiento_x
    if y0< 0 or y1 > ALTURA:
        desplazamiento_y = -desplazamiento_y
    c.move(pelota,desplazamiento_x,desplazamiento_y)

    ventana_principal.after(intervalo, mover_pelota)

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

#dibujar pelota
pelota = c.create_oval(centro_x-RADIO,centro_y-RADIO,centro_x+RADIO,centro_y+RADIO,fill="blue")

#frame de controles
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="black",width=480,height=230)
frame_controles.place(x=10,y=260)

#ejecucion inicial
mover_pelota()

#desplegar ventana pricipal
ventana_principal.mainloop()