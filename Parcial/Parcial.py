from tkinter import *
Base = Tk()

Base.geometry("700x600")
Base.title("Graficadora")
Base.config(bg="cyan3")
Base.iconbitmap("1.ico")
Base.resizable(0,0)


def pendiente():
   X=(X1+X2)/2
   Y=(Y1/Y2)/2 
   print(X,Y)

titulo = Label(Base, text="Recta y Pendiente")
titulo.place(x=300,y=10,width=110,height=30)

recta=Canvas(Base,width=550,height=380)
recta.pack()

X1 = Label(Base, text="Digite X1")
X1.place(x=40,y=420,width=60,height=30)
Y1 = Label(Base, text="Digite Y1")
Y1.place(x=40,y=460,width=60,height=30)

X2 = Label(Base, text="Digite X1")
X2.place(x=40,y=500,width=60,height=30)
Y2 = Label(Base, text="Digite Y2")
Y2.place(x=40,y=540,width=60,height=30)

Z1 = Entry(Base, bg="purple")
Z1.place(x=110,y=420,width=60,height=30)
Z2 = Entry(Base, bg="purple")
Z2.place(x=110,y=460,width=60,height=30)

Z3 = Entry(Base, bg="purple")
Z3.place(x=110,y=500,width=60,height=30)
Z4 = Entry(Base, bg="purple")
Z4.place(x=110,y=540,width=60,height=30)



Base.mainloop()