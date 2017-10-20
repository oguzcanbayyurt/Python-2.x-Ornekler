# -*- coding: utf8 -*-
from Tkinter import*
# Entry(TextBox) ,  Label ,  CheckButton(Checkbox) Kullanımı Hizalanmasi
pencere = Tk()
user = Label(pencere, text = "Kullanici Adi")
passwd = Label(pencere, text = "Sifre")
user.grid(row = 0, column = 0, sticky = E)
passwd.grid(row = 1, column = 0, sticky = E)

entry_1 = Entry(pencere)
entry_2 = Entry(pencere)
entry_1.grid(row = 0, column = 1)
entry_2.grid(row = 1, column = 1)

check1 = Checkbutton(pencere, text = "Beni Hatırla")
check1.grid(columnspan = 2)

pencere.mainloop()
