# -*- coding:utf8 -*-
from Tkinter import *

sayac = 0

def fonk1(buton):
    global sayac
    if sayac % 2 == 0:
      buton["bg"] = "red"
    elif sayac % 5 == 0:
      buton["bg"] = "black"
    else:
        buton["bg"] = "white"
    sayac += 1
    label1["text"] = sayac
    
pencere = Tk()
buton1 = Button(pencere, text = "Tıkla", command = lambda:fonk1(buton1))
buton1.grid(row = 0, column = 0)
label1 = Label(pencere, text = sayac)
label1.grid(row = 0, column = 1)

pencere.mainloop()
