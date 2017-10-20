# -*- coding: utf8 -*-
from Tkinter import *
# Python Penceresinde Menü Oluşturma
pencere = Tk()

def dosyaKaydet():
    print "Dosya Kaydedildi"
def dosyaAc():
    print "DosyA Açıldı"
def geriAl():
    print "İşlem Başarıyla Geri Alındı"

menu = Menu(pencere)
pencere.config(menu = menu)

subMenu = Menu(menu)
menu.add_cascade(label = "Dosya", menu = subMenu)
subMenu.add_command(label = "Dosya Kaydet", command = dosyaKaydet)
subMenu.add_command(label = "Dosya Aç", command = dosyaAc)

subMenu.add_separator()
subMenu.add_command(label = "Çıkış", command = pencere.destroy)

editMenu = Menu(menu)
menu.add_cascade(label = "Düzen", menu = editMenu)
editMenu.add_command(label = "Geri Al", command = geriAl)

pencere.mainloop()
