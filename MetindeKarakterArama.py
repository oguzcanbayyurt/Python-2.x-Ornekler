
metin = "Bilgisayar programciligi programi gece ve gunduz olmak uzere her yil 200 ogrenci ile devam etmektedir."
harf = raw_input("Aranacak karakter")
sayi = ""
for s in metin:
    if harf == s:
        sayi += harf
print(len(sayi))

# ikinci yol
#sayi = 0
#for s in metin:
#    if harf == s:
#        sayi += 1
#print(sayi)
