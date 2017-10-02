# -*- coding: utf8 -*-
import random
rakamlar = range(0, 10)
sonuc = ""
uzunluk = int(raw_input("kaç sayı uzunluğunda olsun"))
for i in range(0, uzunluk):
 sonuc+ = str(random.choice(rakamlar))
print sonuc
