import turtle


from tkinter import*
import math

root = Tk()

root.minsize(width=300, height=200)
root.title("Alakzatok")

can1=Canvas(root,width=200, height=150,bg="white")
photo=PhotoImage(file='hatter4.png')
item=can1.create_image(80,80,image=photo)
can1.pack()

root.minsize(width=200, height=200)
# Háromszög
def harujkerulet():
    abl2 =Toplevel(root)
    abl2.minsize(width=430, height=300)
    L1 = Label(abl2, text="Oldalak hosszúsága")
    L1.pack(side = LEFT)
    E1 = Entry(abl2)
    E1.pack(side = LEFT)
    E2 = Entry(abl2)
    E2.pack(side = RIGHT)
    def harujkerulet():
        a = eval(E1.get())
        eredmeny = a+b+c    
        E2.delete(0,END)
        E2.insert(0,int(eredmeny))
    gomb2 = Button(abl2, text="Kilép", command=abl2.destroy)
    gomb2.pack(side=BOTTOM)
    gomb3 = Button(abl2, text="számítás", command = harujkerulet)
    gomb3.pack(side=LEFT)
    abl2.mainloop()

def harujvalaszto():
    abl3 = Toplevel(root)
    abl3.minsize(width= 100, height=100)
    gomb1 = Button(abl3, text="Kerület", command=harujkerulet)
    gomb1.pack(side= LEFT)
    gomb2 = Button(abl3, text="Terület", command=harujterulet )
    gomb2.pack(side=RIGHT)
    L1 = Label(abl3, text="Kerületet vagy Területet számoljak?")
    L1.pack()
    gomb3 = Button(abl3, text="Kilép", command=abl3.destroy)
    gomb3.pack(side=BOTTOM)
    abl3.mainloop()

def harujterulet():
    abl2 = Toplevel(root)
    abl2.minsize(width=430, height=300)
    L1 = Label(abl2, text="a oldal hosszúsága")
    L1.pack(side = LEFT)
    E1 = Entry(abl2)
    E1.pack(side = LEFT)
    L3 = Label(abl2, text="m magasság hosszúsága")
    L3.pack(side = LEFT)
    E3 = Entry(abl2)
    E3.pack(side = LEFT)
    E4 = Entry(abl2)
    E4.pack(side=TOP)
    def harujterulet():
        a = eval(E1.get())
        ma = eval(E3.get())
        eredmeny = a*ma/2
        E4.delete(0,END)
        E4.insert(0,int(eredmeny))
    gomb2 = Button(abl2, text="Kilép", command=abl2.destroy)
    gomb2.pack(side=BOTTOM)
    gomb3 = Button(abl2, text="számítás", command = harujterulet)
    gomb3.pack(side=LEFT)
    abl2.mainloop()

# Vége

    
def korujablakk():
    def Terulet():
        sugar=eval(E1.get())
        terulet=sugar*sugar*math.pi
        E2.insert(0,str(terulet))
    def Kerulet():
        abl2 =Toplevel(root)
        abl2.minsize(width=430, height=300)
        E1=Entry(abl2)
        E1.pack(side=RIGHT)
        sugar=eval(E1.get())
        kerulet=math.pi*math.pi*sugar
        gomb3.pack(side=BOTTOM)
        E2=Entry(abl2)
        E2.grid(row=0,column=1)
        L2=Label(abl3,text="A kör sugara:")
        L2.pack(side=LEFT)
        E2=Entry(abl2)
        E2.grid(row=1,column=2)
        L3=Label(abl2,text="A kör kerülete:")
        L3.grid(row=2,column=1)
        E3=Entry(abl2)
        E3.grid(row=2,column=2)
    abl3=Toplevel(root)
    abl3.minsize(width= 100, height=100)
    gomb1 = Button(abl3, text="Kerület", command=Kerulet)
    gomb1.pack(side= LEFT)
    gomb2 = Button(abl3, text="Terület", command=Terulet )
    gomb2.pack(side=RIGHT)
    gomb3 = Button(abl3, text="Kilép", command=abl3.destroy)
    gomb3.pack(side=BOTTOM)
    L1 = Label(abl3, text="Kerületet vagy Területet számoljak?")
    L1.pack()

    def Terulet():
        terulet=pi*2*2
        abl2 =Toplevel(abl2)
        abl2.minsize(width=430, height=300)
        E1=Entry(abl2)
        E1.pack(side=RIGHT)
        sugar=eval(E1.get())
        gomb3.pack(side=BOTTOM)
        E2=Entry(abl2)
        E2.grid(row=0,column=1)
        L2=Label(abl3,text="A kör sugara:")
        L2.pack(side=LEFT)

        E2=Entry(abl2)
        E2.grid(row=1,column=2)
        L3=Label(abl2,text="A kör kerülete:")
        L3.grid(row=2,column=1)
        E3=Entry(abl2)
        E3.grid(row=2,column=2)

        abl2.mainloop()

#Négyzet ablak kezdete
#Kerület ablak

def negyukerulet():
    abl2 =Toplevel(root)
    abl2.minsize(width=430, height=300)
    L1 = Label(abl2, text="Oldalak hosszúsága")
    L1.pack(side = LEFT)
    E1 = Entry(abl2)
    E1.pack(side = LEFT)
    E2 = Entry(abl2)
    E2.pack(side = RIGHT)
    def negyzetkerulet():
        a = eval(E1.get())
        eredmeny = a*4    
        E2.delete(0,END)
        E2.insert(0,int(eredmeny))
    gomb2 = Button(abl2, text="Kilép", command=abl2.destroy)
    gomb2.pack(side=BOTTOM)
    gomb3 = Button(abl2, text="számítás", command = negyzetkerulet)
    gomb3.pack(side=LEFT)
    abl2.mainloop()


#Terület vagy kerület kiválasztás ablak


def negyvalaszto():
    abl3 = Toplevel(root)
    abl3.minsize(width= 100, height=100)
    gomb1 = Button(abl3, text="Kerület", command=negyukerulet)
    gomb1.pack(side= LEFT)
    gomb2 = Button(abl3, text="Terület", command=negyterulet )
    gomb2.pack(side=RIGHT)
    L1 = Label(abl3, text="Kerületet vagy Területet számoljak?")
    L1.pack()
    gomb3 = Button(abl3, text="Kilép", command=abl3.destroy)
    gomb3.pack(side=BOTTOM)

    abl3.mainloop()


#Terület ablak


def negyterulet():
    abl2 = Toplevel(root)
    abl2.minsize(width=430, height=300)
    L1 = Label(abl2, text="Oldalak hosszúsága")
    L1.pack(side = LEFT)
    E1 = Entry(abl2)
    E1.pack(side = LEFT)
    E2 = Entry(abl2)
    E2.pack(side = RIGHT)
    def negyzetterulet():
        a = eval(E1.get())
        eredmeny = a*a
        E2.delete(0,END)
        E2.insert(0,int(eredmeny))
    gomb2 = Button(abl2, text="Kilép", command=abl2.destroy)
    gomb2.pack(side=BOTTOM)
    gomb3 = Button(abl2, text="számítás", command = negyzetterulet)
    gomb3.pack(side=LEFT)
    abl2.mainloop()

#Turtle Ide



#Négyzet ablak vége


#Rombusz ablak


#Rombusz felhasználói felület

def romvalaszto():
    abl3 = Toplevel(root)
    abl3.minsize(width= 100, height=100)
    gomb1 = Button(abl3, text="Kerület", command=romkerulet)
    gomb1.pack(side= LEFT)
    gomb2 = Button(abl3, text="Terület", command=romterulet )
    gomb2.pack(side=RIGHT)
    L1 = Label(abl3, text="Kerületet vagy Területet számoljak?")
    L1.pack()
    gomb3 = Button(abl3, text="Kilép", command=abl3.destroy)
    gomb3.pack(side=BOTTOM)

    abl3.mainloop()

#Rombusz területe

def romterulet():
    abl2 = Toplevel(root)
    abl2.minsize(width=430, height=300)
    L1 = Label(abl2, text="Oldalak hosszúsága")
    L1.pack(side = LEFT)
    E1 = Entry(abl2)
    E1.pack(side = LEFT)
    L2 = Label(abl2, text = "Magasság")
    L2.pack(side=LEFT)
    E2 = Entry(abl2)
    E2.pack(side = LEFT)
    E3 = Entry(abl2)
    E3.pack(side= RIGHT)
    def romteruletszam():
        a = eval(E1.get())
        m = eval(E2.get())
        eredmeny = a*m
        E3.delete(0,END)
        E3.insert(0,int(eredmeny))
    gomb2 = Button(abl2, text="Kilép", command=abl2.destroy)
    gomb2.pack(side=BOTTOM)
    gomb3 = Button(abl2, text="számítás", command = romteruletszam)
    gomb3.pack(side=LEFT)
    abl2.mainloop()

#Rombusz Kerülete
def romkerulet():
    abl2 = Toplevel(root)
    abl2.minsize(width=430, height=300)
    L1 = Label(abl2, text="Oldalak hosszúsága")
    L1.pack(side = LEFT)
    E1 = Entry(abl2)
    E1.pack(side = LEFT)
    E3 = Entry(abl2)
    E3.pack(side= RIGHT)
    def romkeruletszam():
        a = eval(E1.get())
        eredmeny = a*4
        E3.delete(0,END)
        E3.insert(0,int(eredmeny))
    gomb2 = Button(abl2, text="Kilép", command=abl2.destroy)
    gomb2.pack(side=BOTTOM)
    gomb3 = Button(abl2, text="számítás", command = romkeruletszam)
    gomb3.pack(side=LEFT)
    abl2.mainloop()

#Rombusz feladat vége


def tarujablak():
    def ujablak():
        abl2 =Toplevel(root)
        gomb2 = Button(abl2, text="Kilép", command=abl2.destroy)
        gomb2.pack(side=TOP)
        abl2.mainloop()
        abl3=Toplevel(root)
        abl3.minsize(width= 100, height=100)
        gomb1 = Button(abl3, text="Kerület",)
        gomb1.pack(side= LEFT)
        gomb2 = Button(abl3, text="Terület",)
        gomb2.pack(side=RIGHT)
        gomb3 = Button(abl3, text="Kilép", command=abl3.destroy)
        gomb3.pack(side=BOTTOM)
        L1 = Label(abl3, text="Kerületet vagy Területet számoljak?")
        L1.pack()

def parujablak():
    abl2 =Toplevel(root)
    gomb2 = Button(abl2, text="Kilép", command=abl2.destroy)
    gomb2.pack(side=TOP)
    abl2.mainloop()
def delujablak():
    abl2 =Toplevel(root)
    gomb2 = Button(abl2, text="Kilép", command=abl2.destroy)
    gomb2.pack(side=TOP)
    abl2.mainloop()
def tegujablak():
    abl2 =Toplevel(root)
    gomb2 = Button(abl2, text="Kilép", command=abl2.destroy)
    gomb2.pack(side=TOP)
    abl2.mainloop()

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Háromszög",command=harujvalaszto)
filemenu.add_command(label="Kör",command=korujablakk)
filemenu.add_command(label="Négyzet",command=negyvalaszto)
filemenu.add_command(label="Rombusz",command=romvalaszto)
filemenu.add_command(label="Trapéz",command=tarujablak)
filemenu.add_command(label="Paralelogramma",command=parujablak)
filemenu.add_command(label="Deltoid",command=delujablak)
filemenu.add_command(label="Téglalap",command=tegujablak)

filemenu.add_separator()
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Alakzatok", menu=filemenu)

Kilepes = Button(root, text="Kilépés", command=exit)
Kilepes.pack()

root.config(menu=menubar)
root.mainloop()
