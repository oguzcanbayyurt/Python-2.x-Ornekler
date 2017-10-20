# -*- coding: utf8 -*-
from Tkinter import *
# Oluşturulan Menüye Durum Çubuğu Ekleme
pencere = Tk()

def dosyaKaydet():
    print "Dosya Kaydedildi"
def dosyaAc():
    print "DosyA Açıldı"
def geriAl():
    print "İşlem Başarıyla Geri Alındı"
def resimYukle():
    print "Resim Yüklenemedi"
def pdfYukle():
    print "Pdf Yüklenemedi"

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

# Araç Çubuğu Kısmı

araccubugu = Frame(pencere, bg = "red")
resimekle = Button(araccubugu, text = "Resim Yükle", command = resimYukle)
resimekle.pack(side = LEFT, padx = 2, pady = 2)

pdfyukle = Button(araccubugu, text = "PDF Yükle", command = pdfYukle)
pdfyukle.pack(side = LEFT, padx = 2, pady = 2)

araccubugu.pack(side = TOP, fill = X)

# Durum Çubuğu Kısmı

durumcubugu = Label(pencere, text = "yukleniyor", bd = 2, relief = SUNKEN, anchor = W)
durumcubugu.pack(side = BOTTOM, fill = X)

pencere.mainloop()
