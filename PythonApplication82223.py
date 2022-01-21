#from tkinter import *
#root = Tk()

#Button(text="Endla:").grid(row=0, column=0)
#table_name = Entry(width=30)
#table_name.grid(row=0, column=1, columnspan=3)

#Button(text="Номер").grid(row=1, column=0)
#table_column = Spinbox(width=7, from_=1, to=50)
#table_column.grid(row=1, column=1)
#Button(text="Квартира").grid(row=1, column=2)
#table_row = Spinbox(width=7, from_=1, to=100)
#table_row.grid(row=1, column=3)

#Button(text="Справка").grid(row=2, column=0)
#Button(text="Вставить").grid(row=2, column=2)
#Button(text="Отменить").grid(row=2, column=2)

#root.mainloop()
from tkinter import *
from tkinter.messagebox import *


root = Tk() #6 i 11
root.title("Tunniplaan")

def urok1(event):
    okno1=Toplevel()
    okno1.grab_set()
    okno1.geometry("275x300")
    logw=Label(okno1, text="Logistikateenused ja varude juhtimine.\nÕpetaja nimi: Inessa Klimanskaja.", width=40,height=20)
    logw.grid(row=0, column=0)
    okno1.mainloop()

def urok2(event):
    okno2=Toplevel()
    okno2.grab_set()
    okno2.geometry("275x300")
    logw=Label(okno2, text="Eesti keel.", width=40,height=20)
    logw.grid(row=0, column=0)
    okno2.mainloop()

def urok3(event):
    okno3=Toplevel()
    okno3.grab_set()
    okno3.geometry("275x300")
    logw=Label(okno3, text="Matemaatika", width=40,height=20)
    logw.grid(row=0, column=0)
    okno3.mainloop()

def urok4(event):
    okno4=Toplevel()
    okno4.grab_set()
    okno4.geometry("275x300")
    logw=Label(okno4, text="Programeerimine alused pliz daite 3", width=40,height=20)
    logw.grid(row=0, column=0)
    okno4.mainloop()

def urok5(event):
    okno5=Toplevel()
    okno5.grab_set()
    okno5.geometry("275x300")
    logw=Label(okno5, text="Fizika", width=40,height=20)
    logw.grid(row=0, column=0)
    okno5.mainloop()

def urok6(event):
    okno6=Toplevel()
    okno6.grab_set()
    okno6.geometry("275x300")
    logw=Label(okno6, text="Russkij", width=40,height=20)
    logw.grid(row=0, column=0)
    okno6.mainloop()

def urok7(event):
    okno7=Toplevel()
    okno7.grab_set()
    okno7.geometry("275x300")
    logw=Label(okno7, text="Fizra", width=40,height=20)
    logw.grid(row=0, column=0)
    okno7.mainloop()

def urok8(event):
    okno8=Toplevel()
    okno8.grab_set()
    okno8.geometry("275x300")
    logw=Label(okno8, text="Keemia", width=40,height=20)
    logw.grid(row=0, column=0)
    okno8.mainloop()

def urok9(event):
    okno9=Toplevel()
    okno9.grab_set()
    okno9.geometry("275x300")
    logw=Label(okno9, text="Excel i word", width=40,height=20)
    logw.grid(row=0, column=0)
    okno9.mainloop()

Label(text="Esmaspaev").grid(row=1, column=0) 
Label(text="Teisipaev").grid(row=2, column=0)
Label(text="Kolmapaev").grid(row=3, column=0)
Label(text="Neljapaev").grid(row=4, column=0)
Label(text="Reede").grid(row=5, column=0)
Label(text="0\n7:40-8:25").grid(row=0, column=1)
Label(text="1\n8:20-9:15").grid(row=0, column=2)
Label(text="2\n9:20-10:05").grid(row=0, column=3)
Label(text="3\n10:10-10:55").grid(row=0, column=4)
Label(text="4\n11:00-11:45").grid(row=0, column=5)
Label(text="5\n11:50-12:35").grid(row=0, column=6)
Label(text="6\n12:40-12:25").grid(row=0, column=7)
Label(text="7\n13:30-14:15").grid(row=0, column=8)
Label(text="8\n14:20-15:05").grid(row=0, column=9)
Label(text="9\n15:10-15:55").grid(row=0, column=10)
estonski=Button(text="Eesti keel", bg="gray", fg="gray")
estonski.grid(row=1, column=2)
logika=Button(root, text="Logistikateenused\nja varude juhtmine", bg="green")
logika.grid(row=1, column=3, columnspan=2)
matemat=Button(text="Matemaatika", bg="pink")
matemat.grid(row=1, column=5)
matemat1=Button(text="Matemaatika", bg="pink")
matemat1.grid(row=1, column=6)
Label(text="").grid(row=1, column=7)
rus1=Button(text="Keel ja\nkirjandus", bg="lightgreen")
rus1.grid(row=1, column=8)
rus2=Button(text="Keel ja\nkirjandus", bg="lightgreen")
rus2.grid(row=1, column=9)
mat1=Button(text="Tugiope\n(matemaatika)", bg="pink")
mat1.grid(row=1, column=10)
himza=Button(text="Tugiope\n(keemia)", bg="purple")
himza.grid(row=1, column=2)
prog1=Button(text="Programeerimise alused(eesti keeles)", bg="lightblue")
prog1.grid(row=2, column=3, columnspan=3)
Label(text="").grid(row=2, column=6)
fiz=Button(text="Fuusika", bg="pink")
fiz.grid(row=2, column=7, columnspan=2)
Button(text="").grid(row=6, column=1)
est1=Button(text="Eesti keel\nkui teine", bg="purple")
est1.grid(row=3, column=2)
Button(text="Kunstiained\n(eesti keeles)", bg="purple").grid(row=3, column=3, columnspan=2)
Label(text="").grid(row=3, column=5)
Button(text="   Kehaline kasvatus   ", bg="purple").grid(row=3, column=6, columnspan=2)
Label(text="").grid(row=4, column=1)
logika1=Button(text="Logistikateenused\nja varude juhtmine", bg="green")
logika1.grid(row=4, column=2, columnspan=2)
Label(text="").grid(row=4, column=3)
prog3=Button(text="Programeerimise alused(eesti keeles)", bg="lightblue")
prog3.grid(row=4, column=4, columnspan=2)
Button(text="Inglise keel\nArenduskeskkonna loomine", bg="pink").grid(row=4, column=6, columnspan=2)
excel=Button(text="Arenduskeskkonna loomine\nEesti keel", bg="pink")
excel.grid(row=4, column=8, columnspan=2)
Label(text="").grid(row=5, column=1)
Button(text="Eesti keel\narenduskeskkonna loomine", bg="pink").grid(row=5, column=2, columnspan=2)
prog2=Button(text=   "Programeerimise alused (eesti keeles)   ", bg="lightblue")
prog2.grid(row=5, column=4, columnspan=5)
excel1=Button(text="arenduskeskkonna loomine\nInglise keel", bg="lightgreen")
excel1.grid(row=5, column=9, columnspan=2)
Exit = Button(root, text = "ВЫХОД", command = root.quit).grid(row = 6, column = 1)

logika.bind("<Button-1>",
           lambda e="Description": urok1(e))
matemat.bind("<Button-1>",
           lambda e="Description": urok3(e))
prog1.bind("<Button-1>",
           lambda e="Description": urok4(e))
fiz.bind("<Button-1>",
           lambda e="Description": urok5(e))
rus1.bind("<Button-1>",
           lambda e="Description": urok6(e))
rus2.bind("<Button-1>",
           lambda e="Description": urok6(e))
mat1.bind("<Button-1>",ub.c
           lambda e="Description": urok3(e))
prog2.bind("<Button-1>",
           lambda e="Description": urok4(e))
prog3.bind("<Button-1>",
           lambda e="Description": urok4(e))
est1.bind("<Button-1>",
           lambda e="Description": urok2(e))
himza.bind("<Button-1>",
           lambda e="Description": urok8(e))
matemat1.bind("<Button-1>",
           lambda e="Description": urok3(e))
logika1.bind("<Button-1>",
           lambda e="Description": urok1(e))
excel.bind("<Button-1>",
           lambda e="Description": urok9(e))
excel1.bind("<Button-1>",
           lambda e="Description": urok9(e))


root.geometry("1200x600")
root.mainloop()

