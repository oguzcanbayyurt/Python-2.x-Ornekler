# -*- coding: utf8 -*-
fark = ""
ilk_metin = "kfgjwıqehrqknşsafqwqqqwelöl,"
ikinci_metin = "asfqsqwrprwş"
for s in ilk_metin:
    if not s in ikinci_metin:
        fark += s
print (fark)
