from tkinter import *

source = Tk()

# Title
label_01 = Label(source, text="Welcome to Python GUI!")
label_01.pack()

# Others things
frame_up = Frame(source)
frame_up.pack()

frame_buttom = Frame(source)
frame_buttom.pack(side=BOTTOM)

# Create the buttoms
buttom_01 = Button(frame_up, text='Click here to test', fg='Blue')
buttom_01.pack(side=LEFT)  # "LEFT" is for up

buttom_02 = Button(frame_buttom, text='Click here to test again', fg='Purple')
buttom_02.pack(side=LEFT)

buttom_03 = Button(frame_buttom, text='Click here to exit', fg='Red')
buttom_03.pack(side=BOTTOM)  # "BOTTOM" is for down

source.mainloop()  # Main menu
