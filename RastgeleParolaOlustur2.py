# -*- coding: cp1254 -*-
import random
import sys
parola=""
sayilar=range(0,10)
ozel=["*","+","?"]
parola_tumu=[]
parola_tumu.extend(sayilar)
parola_tumu.extend(ozel)
kucukharfler=range(97,123)
buyukharfler=range(65,91)
for i in range(0,len(kucukharfler)):
 parola_tumu.append(chr(kucukharfler[i]))
 parola_tumu.append(chr(buyukharfler[i]))
try:
 uzunluk=int(raw_input("Parola Uzunluğu"))
except ValueError:
 print "Hatalı Giriş"
 sys.exit()
uret=random.sample(parola_tumu,uzunluk)
for a in uret:
    parola+=str(a)
print parola
 
