# -*- coding: utf8 -*-
from Tkinter import*
# Entry(TextBox) ,  Label Kullanımı Hizalanmasi
pencere = Tk()
user = Label(pencere, text = "Kullanici Adi")
passwd = Label(pencere, text = "Sifre")
user.grid(row = 0, column = 0)
passwd.grid(row = 1, column = 0)

entry_1 = Entry(pencere)
entry_2 = Entry(pencere)
entry_1.grid(row = 0, column = 1)
entry_2.grid(row = 1, column = 1)

pencere.mainloop()
