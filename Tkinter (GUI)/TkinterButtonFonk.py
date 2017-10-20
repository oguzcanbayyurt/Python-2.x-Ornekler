# -*- coding: utf8 -*-
from Tkinter import*
# herhangi bir butona fonksiyon kullanarak parametresiz bir şekilde olay atama
pencere = Tk()
def yazdir():
    print  "Butona Basildi"

buton = Button(pencere, text = "Giris", command = yazdir)
buton.pack()

pencere.mainloop()
