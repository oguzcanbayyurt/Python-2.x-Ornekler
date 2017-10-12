# -*- coding: utf8 -*-
d1 = open("dosya1.txt")
d1_satirlar = d1.readlines()
d2 = open("dosya2.txt")
d2_satirlar = d2.readlines()
d1_harfler = ""
d2_harfler = ""
fark = ""
for satir in d1_satirlar:
    for harf in satir:
        if not harf in d1_harfler:
            d1_harfler += harf
        if not harf in d2_harfler:
            d2_harfler += harf
for harf in d1_harfler:
    if not harf in d2_harfler:
        fark += harf
print fark
d1.close()
d2.close()
