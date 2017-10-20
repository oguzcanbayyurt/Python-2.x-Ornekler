# -*- coding: utf8 -*-
from Tkinter import*
# Bind ile herhangi bir nesneye olay ekleme
#(Command Kullanılmaz,  Fonksiyonda Parametre olur, Event)
pencere = Tk()
def yazdir1(event):
    print  "Sol Tıklandı"
def yazdir2(event):
    print  "Sag Tıklandı"

buton = Button(pencere, text = "Giris")
buton.bind("<Button-1>", yazdir1)
buton.bind("<Button-3>", yazdir2)
buton.pack()

pencere.mainloop()
