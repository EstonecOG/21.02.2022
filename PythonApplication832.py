s#from tkinter import *
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
root.title("Raspisanie")


def est(event):
        win20=Toplevel()
        win20.grab_set()
        win20.geometry("275x300")
        estw=Label(win20, text="Tunni nimetus: Eesti keel II grupp.\nÕpetaja nimi: Olesja Ojamäe.\nKabinet: B 234", width=40,height=20)
        estw.grid(row=0, column=0)
        win20.mainloop()

def ruhm(event):
        win32=Toplevel()
        win32.grab_set()
        win32.geometry("275x300")
        ruhm=Label(win32, text="Tunni nimetus: Rühmajunhatajantund.\nÕpetaja nimi: Alina Laaneväli.\nKabinet: B 236", width=40,height=20)
        ruhm.grid(row=0, column=0)
        win32.mainloop()
    
def log(event):
        win4=Toplevel()#создаём второе(дочернее) окно
        win4.grab_set()#не позволяет закрыть основное окно, пока не закроем дочернее окно
        win4.geometry("275x300")
        logw=Label(win4, text="Logistikateenused ja varude juhtimine.\nÕpetaja nimi: Inessa Klimanskaja.\nKabinet: B 002", width=40,height=20)
        logw.grid(row=0, column=0)
        win4.mainloop()

log1=Label(win2, borderwidth=1, bg="#80e092", relief="solid",text="Logistikateenused\nja varude juhtimine", width=10,height=8)
log1.grid(row=1, column=3, sticky=N+S+W+E, columnspan=2)
log1.bind("<Button-1>",lambda e="Description": log(e))#


Label(text="Понедельник").grid(row=1, column=0) 
Label(text="Вторник").grid(row=2, column=0)
Label(text="Среда").grid(row=3, column=0)
Label(text="Четверг").grid(row=4, column=0)
Label(text="Пятница").grid(row=5, column=0)
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
Button(text="Eesti keel", bg="gray", fg="gray").grid(row=1, column=2)
est=Button(text="Logistikateenused\nja varude juhtmine", bg="green").grid(row=1, column=3, columnspan=2)
Button(text="Matemaatika", bg="pink").grid(row=1, column=5)
Button(text="Matemaatika", bg="pink").grid(row=1, column=6)
Label(text="").grid(row=1, column=7)
Button(text="Keel ja\nkirjandus", bg="lightgreen").grid(row=1, column=8)
Button(text="Keel ja\nkirjandus", bg="lightgreen").grid(row=1, column=9)
Button(text="Tugiope\n(matemaatika)", bg="pink").grid(row=1, column=10)
Button(text="Tugiope\n(keemia)", bg="purple").grid(row=1, column=2)
Button(text="Programeerimise alused(eesti keeles)", bg="lightblue").grid(row=2, column=3, columnspan=3)
Label(text="").grid(row=2, column=6)
Button(text="Fuusika", bg="pink").grid(row=2, column=7, columnspan=2)
Button(text="").grid(row=6, column=1)
Button(text="Eesti keel\nkui teine", bg="purple").grid(row=3, column=2)
Button(text="Kunstiained\n(eesti keeles)", bg="purple").grid(row=3, column=3, columnspan=2)
Label(text="").grid(row=3, column=5)
Button(text="   Kehaline kasvatus   ", bg="purple").grid(row=3, column=6, columnspan=2)
Label(text="").grid(row=4, column=1)
Button(text="Logistikateenused\nja varude juhtmine", bg="green").grid(row=4, column=2, columnspan=2)
Label(text="").grid(row=4, column=3)
Button(text="Programeerimise alused(eesti keeles)", bg="lightblue").grid(row=4, column=4, columnspan=2)
Button(text="Inglise keel\nArenduskeskkonna loomine", bg="pink").grid(row=4, column=6, columnspan=2)
Button(text="Arenduskeskkonna loomine\nEesti keel", bg="pink").grid(row=4, column=8, columnspan=2)
ruhm=Button(ruhm, text="Ruhmajuhataja tund", bg="purple").grid(row=4, column=11)
ruhm.grid(row=4, column=11, sticky=N+S+W+E)
Label(text="").grid(row=5, column=1)
Button(text="Eesti keel\narenduskeskkonna loomine", bg="pink").grid(row=5, column=2, columnspan=2)
Button(text=   "Programeerimise alused (eesti keeles)   ", bg="lightblue").grid(row=5, column=4, columnspan=5)
Button(text="arenduskeskkonna loomine\nInglise keel", bg="lightgreen").grid(row=5, column=9, columnspan=2)
Exit = Button(root, text = "ВЫХОД", command = root.quit).grid(row = 6, column = 1)
log1.grid(row=1, column=3, sticky=N+S+W+E, columnspan=2)
log1.bind("<Button-1>",lambda e="Description": log(e))#


root.geometry("1200x600")
root.mainloop()