# -*- coding: utf8 -*-
cevap = "sezer"
print "giris yapmak icin kullanici adini yaziniz"
girilen_isim = raw_input()
if cevap == girilen_isim:
    print "Islem Başarılı"
else:
    print " Islem Basarısız 2 Hakkiniz Kaldi"
    girilen_isim = raw_input()
    if cevap == girilen_isim:
        print "Islem Basarili"
    else:
        print " Islem Basarısız 1 Hakkiniz Kaldi"
        girilen_isim = raw_input()
        if cevap == girilen_isim:
            print "Islem Basarili"
        else:
            print " Islem Basarısız Hakkiniz Doldu"
        
    
