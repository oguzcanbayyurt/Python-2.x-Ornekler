# -*- coding: cp1254 -*-,
print "��kmak ��in 999 Giriniz"
deger = 0
sayac = 0
while True:
 sayi = int(raw_input("say� giriniz"))
 if sayi == 999:
     break
 elif sayi > deger:
     deger = sayi
 sayac += 1
print "{0} Say� Girdiniz, Bunlardan En B�y��� = {1}".format(sayac, deger)
