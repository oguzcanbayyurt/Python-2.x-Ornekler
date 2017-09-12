# -*- coding: cp1254 -*-,
print "Çıkmak İçin 999 Giriniz"
deger = 0
sayac = 0
while True:
 sayi = int(raw_input("sayı giriniz"))
 if sayi == 999:
     break
 elif sayi > deger:
     deger = sayi
 sayac += 1
print "{0} Sayı Girdiniz, Bunlardan En Büyüğü = {1}".format(sayac, deger)
