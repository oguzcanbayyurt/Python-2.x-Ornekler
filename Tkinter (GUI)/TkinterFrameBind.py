# -*- coding: utf8 -*-
from Tkinter import*
# Buton ve klavye yardımıyla,  butona basıldığında pencere içerisindeki framenin
# x ve y  eksenindeki kordinaatlarını veren,  klavyeden herhangi bir tuşa basıl
# dığında basılan tuşu ekrana yazdıran programnın bind kullanılarak hazırlanması
pencere = Tk()
def tusabas(event):
    print  "basildi", repr(event.char)
def tiklama(event):
    frame.focus_set()
    print "Tiklandi", event.x, event.y

frame = Frame(pencere, width = 100, height = 100)
frame.bind("<Key>", tusabas)
frame.bind("<Button-1>", tiklama)
frame.pack()

pencere.mainloop()
