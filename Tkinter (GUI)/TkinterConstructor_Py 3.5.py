# -*- coding: utf8 -*-
import tkinter as tk
# Constructor Kullanımı

pencere = tk.Tk()

class abc:
    def __init__(self, pencere):
        frame = tk.Frame(pencere)
        frame.pack()

        self.button = tk.Button(frame, text = "Giriş", command = self.butmsg)
        self.button.pack()

        self.cikisbutton = tk.Button(frame, text = "Çıkış", command = pencere.destroy, bg = "blue", fg = "white")
        self.cikisbutton.pack()
    def butmsg(self):
        print ("Giriş Yapıldı")
s = abc(pencere)
pencere.mainloop()
