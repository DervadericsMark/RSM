from tkinter import*

root = Tk()

root.minsize(width=400, height=400)

menubar = Menu(root)

filemenu = Menu(menubar, tearoff=0)

filemenu.add_command(label="Kör")

filemenu.add_command(label="Négyzet")

filemenu.add_command(label="Rombusz")

filemenu.add_command(label="Háromszög")

filemenu.add_command(label="Trapéz")

filemenu.add_command(label="Paralelogramma")

filemenu.add_command(label="Deltoid")

filemenu.add_command(label="Téglalap")

filemenu.add_command(label="Kilépés", command=exit)


filemenu.add_separator()

editmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Alakzatok", menu=filemenu)




root.config(menu=menubar)

root.mainloop()
