from tkinter import*

root = Tk()

root.minsize(width=200, height=200)

def harujablak():
    abl2 =Toplevel(root)
    gomb2 = Button(abl2, text="Kilép", command=abl2.destroy)
    gomb2.pack(side=TOP)
    abl2.mainloop()

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Háromszög",command=harujablak)
filemenu.add_command(label="Kör",command=)
filemenu.add_command(label="Négyzet",command=)
filemenu.add_command(label="Rombusz",command=)
filemenu.add_command(label="Trapéz",command=)
filemenu.add_command(label="Paralelogramma",command=)
filemenu.add_command(label="Deltoid",command=)
filemenu.add_command(label="Téglalap",command=)

filemenu.add_separator()
editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Alakzatok", menu=filemenu)

Kilepes = Button(root, text="Kilépés", command=exit)
Kilepes.pack()

root.config(menu=menubar)
root.mainloop()
