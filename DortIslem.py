# -*- coding: cp1254 -*-
topla = "{1}Toplama"
cikarma = "{2}Çıkarma"
carpma = "{3}Çarpma"
bolme = "{4}Bölme"

print topla
print cikarma
print carpma
print bolme
sor = raw_input("Lütfen İşlem Seçiniz:")
if sor == "1":
    sayi1 = input("1.Sayıyı Girin:")
    sayi2 = input("2.Sayıyı Girin:")
    print sayi1, " + ", sayi2," = ", sayi1+sayi2
if sor == "2":
    sayi1 = input("1.Sayıyı Girin:")
    sayi2 = input("2.Sayıyı Girin:")
    print sayi1, " - ", sayi2, " = ", sayi1-sayi2
if sor == "3":
    sayi1=input("1.Sayıyı Girin:")
    sayi2=input("2.Sayıyı Girin:")
    print sayi1, " * ", sayi2, " = ", sayi1*sayi2
if sor == "4":
    sayi1 = input("1.Sayıyı Girin:")
    sayi2 = input("2.Sayıyı Girin:")
    print sayi1, " / ", sayi2, " = ", sayi1/sayi2
