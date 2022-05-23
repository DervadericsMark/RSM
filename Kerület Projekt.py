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
def negyujablak():
    abl2 =Toplevel(root)
    abl2.minsize(width=200, height=200)
    gomb2 = Button(abl2, text="Kilép", command=abl2.destroy)
    gomb2.pack(side=TOP)
    abl2.mainloop()
def negykerulet():
    sz1 = Label(negyujablak, text = "a:")
    sz2 = Label(negyujablak, text='Eredmény:')
    m1= Entry(negyujablak)
    m2= Entry(negyujablak)
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
filemenu.add_command(label="Négyzet",command=negyujablak)
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
