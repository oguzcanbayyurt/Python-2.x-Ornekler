hakkinda = open("hakkinda.txt")
harf = raw_input("Aranacak Harf:")
sayi = 0
for karakter_dizisi in hakkinda:
    for karakter in karakter_dizisi:
        if harf == karakter:
            sayi += 1
print (sayi)
hakkinda.close()
