from tkinter import *

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

#linearecta
linea_1= c.create_line(BASE/2,ALTURA/2,BASE,0,fill="red",width=2)
linea_2= c.create_line(0,0,BASE/2,ALTURA/2,fill="green",width=2)

#dibujar texto
texto_1 =c.create_text(BASE/4,ALTURA/4,anchor="center",text="miguel galvis",font=("arial",25,"bold"),fill="blue",activefill="yellow")

#rectagulos dibujo
rectangulo_1 =c.create_rectangle(BASE/2,ALTURA/2,BASE,ALTURA,fill="pink",outline="blue")

#poligono
poligono_1 = c.create_polygon(0,0,BASE/2,ALTURA/2,0,ALTURA,fill="red",outline="red")

#circulo
circulo_1 =c.create_oval(BASE/2-50,ALTURA/2-50,BASE/2+50,ALTURA/2+50,fill="orange",outline="green")

#arcos
arco_1=c.create_arc(BASE/2-30,ALTURA/2-30,BASE/2+30,ALTURA/2+30,start=30,extent=300,fill="black")

#frame de controles
frame_controles = Frame(ventana_principal)
frame_controles.config(bg="black",width=480,height=230)
frame_controles.place(x=10,y=260)

#desplegar ventana pricipal
ventana_principal.mainloop()

