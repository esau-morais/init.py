# coding=utf-8
from tkinter import *

source = Tk()


# Create a function
def print_name(event):
    print("Esaú Morais")


button_1 = Button(source, text='Name')
button_1.bind('<Button-1>', print_name)
button_1.pack()

source.mainloop()
