# -*- coding: cp1254 -*-
kac_sayigirilecek = raw_input("Kaç Sayı Girilecek:")
sayilar = []
toplam_teksayilar = 0
toplam_ciftsayilar = 0
for sayi in range(0, int(kac_sayigirilecek)):
  sayilar.append(int(raw_input("{0}. sayıyı giriniz".format(sayi+1))))
  if sayilar[sayi] % 2 == 0:
    toplam_ciftsayilar = toplam_ciftsayilar + sayilar[sayi]
  else:
    toplam_teksayilar = toplam_teksayilar + sayilar[sayi]
print "Tek Sayıların Toplamı:{0}\n" \
      "Çift Sayıların Toplamı:{1}\n" \
      "Toplamda {2} sayı girildi.".format(toplam_teksayilar,toplam_ciftsayilar,kac_sayigirilecek)
