# -*- coding: cp1254 -*-
try:
    metinsayisi = int(raw_input("kac metin girilecek"))
    metinler = []
    uzunluklar = []
    uzunluk = 0
    for i in range(0, metinsayisi):
       metinler.append(raw_input("{0}. metin giriniz".format(i+1)))
       uzunluklar.append( len(metinler[i]) )
       if uzunluklar[i] >= uzunluk:
         uzunluk = uzunluklar[i]
         index = i
    print "en uzun metin:{0} karakter sayısı: {1}".format(metinler[index], uzunluk)
except ValueError:
    print "Sayı Girmeniz Gerekmektedir"
    

