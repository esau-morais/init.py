from tkinter import *

source = Tk()

# Create the label
label_01 = Label(source, text='User: ')
label_02 = Label(source, text='Password: ')

# Grid 
label_01.grid(row=0)
label_02.grid(row=1)

# Create the entry
entry_01 = Entry(source)
entry_02 = Entry(source)

# Grid
entry_01.grid(row=0, column=1)
entry_02.grid(row=1, column=1)

# Keep
check = Checkbutton(source, text='Keep me signed in')
check.grid(columnspan=2)

source.mainloop()
