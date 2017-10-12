d1 = open("isimler1.txt")
d1_satirlar = d1.readlines()
d2 = open("isimler2.txt")
d2_satirlar = d2.readlines()
for harf in d2_satirlar:
    if not harf in d1_satirlar:
        print (i)
d1.close()
d2.close()
