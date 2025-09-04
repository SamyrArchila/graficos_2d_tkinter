from tkinter import *

#variables globales
BASE = 460
ALTURA = 460

# ventana pricipal
ventana_principal = Tk()
ventana_principal.title("samyr archila")
ventana_principal.resizable(False,False)
ventana_principal.geometry("700x600")
ventana_principal.config(bg="lightblue")


# Frame de graficación
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="lightblue",width=670,height=670)
frame_graficacion.place(x=10,y=10)

#lienzo de graficacion
c =Canvas(frame_graficacion,width=BASE,height=ALTURA)
c.config(bg="lightblue")
c.place(x=10,y=10)


rectangulo_1 = c.create_rectangle(80,300,300,200,fill="red", outline="blue")
rectangulo_2 = c.create_rectangle(180,130,290,200,fill="green")
rectangulo_3 = c.create_rectangle(171,100,300,130,fill="pink")
rectangulo_4 = c.create_rectangle(182,80,290,100,fill="white")

texto_1 = c.create_text(BASE/2.5, ALTURA/1.7,anchor="center", text="Samyr Archila", font=("Arial", 25, "bold"), fill="white" , activefill="yellow")

#desplegar ventana pricipal
ventana_principal.mainloop()



























ventana_principal.mainloop()