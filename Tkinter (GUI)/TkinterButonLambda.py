# -*- coding:utf8 -*-
from Tkinter import*
import tkMessageBox

def a(deger):
    deger["text"] = "Buna Tıkladın"
    deger["bg"] = "firebrick"
    deger["fg"] = "white"
    deger["bd"] = 10
    deger["relief"] = SUNKEN
    deger["anchor"] = W
    
pencere = Tk()
buton1 = Button(pencere, text = "1.Tıkla", command = lambda:a(buton1))
buton1.pack()
buton2 = Button(pencere, text = "2.Tıkla", command = lambda:a(buton2))
buton2.pack()

pencere.mainloop()
