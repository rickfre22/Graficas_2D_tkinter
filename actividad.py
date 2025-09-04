from tkinter import *
ventana= Tk()
ventana.title("trencito")
ventana.resizable(False,False)
ventana.geometry("500x500")
ventana.config(bg="white")

#canva
c = Canvas(ventana,width=480,height=480)
c.config(bg="skyblue")
c.place(x=10,y=10)

#tierr
tierr=c.create_rectangle(0,300,480,480,fill="green",outline="green")

#base tren
base = c.create_rectangle(90,250,500,380,fill="gray",outline="gray")
base2 = c.create_rectangle(125,240,400,390,fill="lightgray",outline="lightgray")
frente=c.create_rectangle(120,240,100,390,fill="darkgray",outline="darkgray")
cabina = c.create_rectangle(240,150,390,240,fill="gray",outline="gray")
cabina2 = c.create_rectangle(250,160,380,230,fill="white",outline="gray")
techo =c.create_rectangle(230,140,400,150,fill="darkgray",outline="darkgray")
techo2 =c.create_rectangle(240,130,390,140,fill="darkgray",outline="darkgray")
llanta =c.create_oval(150,350,230,430,fill="black")
rin1=c.create_oval(160,360,220,420,fill="gray")
llanta2 =c.create_oval(240,350,320,430,fill="black")
bagon = c.create_rectangle(420,240,500,390,fill="lightgray",outline="lightgray")
rin2 = c.create_oval(250,360,310,420,fill="gray")
llanta3 =c.create_oval(330,350,410,430,fill="black")
rin3 =c.create_oval(340,360,400,420,fill="gray")
eje1 = c.create_rectangle(190,385,270,400,fill="ivory",outline="lightgray")
eje2 = c.create_rectangle(290,385,370,400,fill="ivory",outline="lightgray")
texto_1 =c.create_text(250,300,anchor="center",text="miguel galvis",font=("arial",25,"bold"),fill="blue",activefill="lightgray")
mataburro = c.create_polygon(100,350,100,420,10,420,fill="darkgray",outline="darkgray")
ventana.mainloop()