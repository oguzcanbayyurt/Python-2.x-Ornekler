# -*- coding: utf8 -*-
import random
import sys
parola = ""
uzunluk = ""
parola_tumu = []
parola_ls = []
uret = []
sayilar = range(0, 10)
kucuk_harfler = range(97, 123)
buyuk_harfler = range(65, 91)
ozel_karakter = ["!", "#", "+", "$", "&", "*", "?", "-", "_"]
for i in range(0, len(kucuk_harfler)):
    parola_tumu.append(chr(kucuk_harfler[i]))
    parola_tumu.append(chr(buyuk_harfler[i]))
    try:
        parola_tumu.append(sayilar[i])
    except IndexError:
        pass
    try:
        parola_tumu.append(ozel_karakter[i])
    except IndexError:
        pass
    try:
        uzunluk = int(raw_input("Parola Uzunluğu Kaç Karakter Olsun?:"))
    except ValueError:
        print "Bir Sayı Girmeniz Gerekmektedir"
        sys.exit()
    uret = random.sample(xrange(0, len(parola_tumu)), uzunluk)
    for i in range(0, uzunluk):
        parola_ls.append(parola_tumu[uret[i]])
        parola = parola + str(parola_ls[i])
    print "uretilen parola:%s"%(parola)
        
