# -*- coding: cp1254 -*-
topla = "{1}Toplama"
cikarma = "{2}��karma"
carpma = "{3}�arpma"
bolme = "{4}B�lme"

print topla
print cikarma
print carpma
print bolme
sor = raw_input("L�tfen ��lem Se�iniz:")
if sor == "1":
    sayi1 = input("1.Say�y� Girin:")
    sayi2 = input("2.Say�y� Girin:")
    print sayi1, " + ", sayi2," = ", sayi1+sayi2
if sor == "2":
    sayi1 = input("1.Say�y� Girin:")
    sayi2 = input("2.Say�y� Girin:")
    print sayi1, " - ", sayi2, " = ", sayi1-sayi2
if sor == "3":
    sayi1=input("1.Say�y� Girin:")
    sayi2=input("2.Say�y� Girin:")
    print sayi1, " * ", sayi2, " = ", sayi1*sayi2
if sor == "4":
    sayi1 = input("1.Say�y� Girin:")
    sayi2 = input("2.Say�y� Girin:")
    print sayi1, " / ", sayi2, " = ", sayi1/sayi2
