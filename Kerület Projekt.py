import turtle


from tkinter import*
import math

root = Tk()

<<<<<<< HEAD
=======
root.minsize(width=300, height=200)
root.title("Alakzatok")
>>>>>>> 615db6c69bde3bb5825f3990e069a2c1b309a16d

can1=Canvas(root,width=200, height=150,bg="white")
photo=PhotoImage(file='hatter4.png')
item=can1.create_image(80,80,image=photo)
can1.pack()

root.minsize(width=200, height=200)
def harujablak():


    abl2 =Toplevel(root)
    L1 = Label(abl2, text="1. oldal")
    L1.pack( side = LEFT)
    E1 = Entry(abl2, bd =5)
    E1.pack(side = RIGHT)

    gomb2 = Button(abl2, text="Kilép", command=abl2.destroy)
    gomb2.pack(side=TOP)

    abl2.mainloop()
def korujablak():    
    abl2 =Toplevel(root)
    gomb2 = Button(abl2, text="Kilép", command=abl2.destroy)
    gomb2.pack(side=TOP)
    def korsugar():
        sugara = int(sugar.get())
        magassaga = int(magassag.get())
        eredmeny = pi * sugara * sugara * magassaga
    def korterulet():
        sugara*sugara*pi
    def korkerulet():


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

#Turtle Ide majd Márk légyszi, köszi



#Négyzet ablak vége



def rombujablak():
    abl2 =Toplevel(root)
    gomb2 = Button(abl2, text="Kilép", command=abl2.destroy)
    gomb2.pack(side=TOP)
    abl2.mainloop()
def tarujablak():
    abl2 =Toplevel(root)
    gomb2 = Button(abl2, text="Kilép", command=abl2.destroy)
    gomb2.pack(side=TOP)
    abl2.mainloop()
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
filemenu.add_command(label="Háromszög",command=harujablak)
filemenu.add_command(label="Kör",command=korujablak)
filemenu.add_command(label="Négyzet",command=negyvalaszto)
filemenu.add_command(label="Rombusz",command=rombujablak)
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
