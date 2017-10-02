import os

program = input("Program Adını Giriniz")

def calistir(program):
    isim = program + ".exe"
    os.startfile(isim)
    print (isim, " Açıldı")
    
calistir(program)

