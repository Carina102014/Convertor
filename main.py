from tkinter import *

window = Tk()

window.title("binary to decimal")

window.geometry("350x350")

nr1_label = Label (window, text="decimal number:")
nr1_label.place(x=20,y=60)

nr1_entry = Entry (window)
nr1_entry.place(x=120,y=60)

nr2_label = Label (window, text ="binary number: ")
nr2_label.place(x=20,y=80)

nr2_label = Label (window, text=" ")
nr2_label.place(x=120,y=80)

def binary():
    binarnr=bin(int((nr1_entry).get()))[2:]
    nr2_label.config(text=binarnr)

buton_binary=Button(window, text="convert", command=binary)
buton_binary.place(x=190,y=120)


window.mainloop()