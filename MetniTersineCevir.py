# -*- coding: cp1254 -*-
metin = raw_input("metin giriniz:")
liste = []
yeni = ""
for harf in metin:
 liste.append(harf)
liste.reverse()
for a in liste:
    yeni+ = a
print "Tersi:", yeni

# Kısa yol
print metin[::-1]
