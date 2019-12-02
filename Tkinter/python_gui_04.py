from tkinter import *

source = Tk()

# Create three functions

def print_left(event):
    print('Left')


def print_middle(event):
    print('Middle')


def print_right(event):
    print('Right')


frame_buttons = Frame(source, width=300, height=250)
frame_buttons.bind('<Button-1>', print_left)
frame_buttons.bind('<Button-2>', print_middle)
frame_buttons.bind('<Button-3>', print_right)
frame_buttons.pack()

source.mainloop()
