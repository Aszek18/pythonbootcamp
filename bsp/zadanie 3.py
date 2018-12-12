import tkinter


def funkcja():
    cena = int(cena.get())
    spalanie= int(spalanie.get())
    dystans = int(dystans.get())
    wynik =  cena * spalanie * dystans
    label.configure(wynik)

root = tkinter.Tk()
root.columnconfigure(1)

cena = tkinter.Entry(master=root)
cena.grid(row=0, column=0)

dystans = tkinter.Entry(master=root)
cena.grid(row=0, column=1)

spalanie = tkinter.Entry(master=root)
spalanie.grid(row=0, column=2)

label = tkinter.Label (master=root, text = "wynik")

button_cena = tkinter.Button(master=root, text = "cena", command = funkcja)
button_dystans = tkinter.Button(master=root, text = "dystans", command = funkcja)
button_spalanie = tkinter.Button(master=root, text = "spalanie", command = funkcja)
button_wynik= tkinter.Button(master=root, text = "wynik", command = funkcja)

button_wynik.grid(row=1,column=0)
label.grid(row=0, column=1)
root.mainloop()