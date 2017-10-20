from Tkinter import*
# 3 Butonun Sola Hizalanmasi (side = LEFT)
pencere = Tk()
cerceve1 = Frame(pencere)
cerceve1.pack()
cerceve2 = Frame(pencere)
cerceve2.pack(side = BOTTOM)

button1 = Button(cerceve1, text = "Anasayfa", fg = "red")
button2 = Button(cerceve1, text = "Ekle", fg = "blue")
button3 = Button(cerceve1, text = "Sil", fg = "purple")
button4 = Button(cerceve2, text = "Cikis", fg = "green")

button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)
button4.pack()

pencere.mainloop()
