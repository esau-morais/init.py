try:
    from tkinter import *
    from sqlite3 import *
    from tkinter import messagebox
    import os
    import sqlite3 as sq
    from emoji import *
except:
    print()

class Functions():
    def __init__(self, master=None): # Function #1
        self.main_window = Frame(master) 
        self.main_window.pack() 

        window.resizable(0, 0)

        window.bind('<Control-r>', self.active_button_02)

        window.bind('<Control-l>', self.active_button)

        window.bind('<Control-i>', self.info_menu)

        window.bind('<Control-x>', quit)

        self.main_font = ('Welcome', 120) # Main font: to the main label

        self.alternative_font = ('Courier 10 Pitch', 18) # Alternative font: to the buttons

        self.main_window = window.title('My Python GUI') # Window title

        self.main_window = window.geometry('800x500') # Window size

        self.main_window = window.configure(bg='#005484') # Window background

        self.main_window_icon = PhotoImage(file=os.path.join(r'/home/esau_morais/Área de Trabalho/Python/My Python GUI/main_icon.png'))
        window.call('wm', 'iconphoto', window._w, self.main_window_icon)

        self.main_window_image = PhotoImage(file='/home/esau_morais/Área de Trabalho/Python/My Python GUI/background.gif')

        self.main_window_background = Label(self.main_window, image=self.main_window_image)
        self.main_window_background.place(x=0, y=0, relwidth=1, relheight=1)

        self.menu = Menu(self.main_window, bg='#005484', fg='White' ,activebackground='#005484', activeforeground='White')

        window.config(menu=self.menu)

        self.sub_menu = Menu(self.menu, activebackground='#005484', bg='#005484', fg='White' ,activeforeground='White')

        self.menu.add_cascade(label='User Account', menu=self.sub_menu)

        self.sub_menu.add_command(label='Login', command=self.active_button)

        self.sub_menu.add_command(label='Sign Up', command=self.active_button_02)

        self.separator = self.sub_menu.add_separator()

        self.sub_menu.add_command(label='Exit', command=quit)

        self.sub_menu_02 = Menu(self.menu, activebackground='#005484', bg='#005484', activeforeground='White')
        self.sub_menu_02['fg'] = ('White')

        self.menu.add_cascade(label='Help', menu=self.sub_menu_02)

        self.sub_menu_02.add_command(label='Info', command=self.info_menu)

        self.sub_menu_02.add_command(label='Help me', command=self.help_menu)

        self.sub_menu_03 = Menu(self.menu, activebackground='#005484', bg='#005484', fg='White', activeforeground='White', disabledforeground='White')

        self.menu.add_cascade(label='Shortcuts', menu=self.sub_menu_03)

        self.sub_menu_03.add_command(label='User Login → Ctrl + L', command=self.active_button, state=DISABLED)

        self.sub_menu_03.add_command(label='User Register → Ctrl + R', command=self.active_button_02, state=DISABLED)

        self.sub_menu_03.add_command(label='Info → Ctrl + I', command=self.info_menu, state=DISABLED)

        self.sub_menu_03.add_command(label='Close (All windows) → Ctrl + X', command=quit, state=DISABLED)

        self.sub_menu_03.add_command(label='Close (Window in focus) → Alt + F4', state=DISABLED)

        self.photo_01 = PhotoImage(file='/home/esau_morais/Área de Trabalho/Python/My Python GUI/icon.png')

        self.pass_button = Frame(master)
        self.pass_button.pack(side=BOTTOM)

        self.button_01 = Button(self.pass_button, text='Login' ,highlightthickness=0,
        highlightbackground='White', activebackground='#005484',relief=FLAT, 
        image=self.photo_01, compound=LEFT, anchor=CENTER, activeforeground='White')        
        self.button_01['font'] = self.alternative_font
        self.button_01['bg'] = ('#005484')
        self.button_01['fg'] = ('White')
        self.button_01['width'] = 260
        self.button_01['height'] = 330
        self.button_01['command'] = self.active_button
        self.button_01.pack(side=LEFT)

        self.button_02 = Button(self.pass_button, text='Register' ,highlightthickness=0, 
        highlightbackground='White', activebackground='#005484' ,relief=FLAT,  
        image=self.photo_01, compound=LEFT, anchor=CENTER, activeforeground='White')
        self.button_02['font'] = self.alternative_font
        self.button_02['bg'] = ('#005484')
        self.button_02['fg'] = ('White')
        self.button_02['width'] = 260
        self.button_02['height'] = 330
        self.button_02['command'] = self.active_button_02
        self.button_02.pack(side=RIGHT)

        self.main_title = Label(self.main_window, text='Welcome!', bg='#005484') # Main label background
        self.main_title['font'] = self.main_font
        self.main_title['fg'] = ('White')
        self.main_title['pady'] = 30
        self.main_title.pack(side=TOP)

    def active_button(self, master=None): # Function #2
        self.new_main_window = Toplevel()

        self.new_main_window.bind('<Control-r>', self.active_button_02)

        self.new_main_window.bind('<Control-i>', self.info_menu)

        self.new_main_window.bind('<Control-x>', quit)

        self.new_main_window.resizable(0, 0)

        self.main_window_02 = self.new_main_window.title('User Login')

        self.main_window_02 = self.new_main_window.geometry('700x400')

        self.main_window_02 = self.new_main_window.configure(bg='#005484')
        
        self.new_main_window_background = PhotoImage(file='/home/esau_morais/Área de Trabalho/Python/My Python GUI/background.gif')

        self.new_main_window_label = Label(self.new_main_window, image=self.new_main_window_background)
        self.new_main_window_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.label_01 = Label(self.new_main_window, text='User Login'.center(15), font=('Chilanka', 28))
        self.label_01['bg'] = ('#005484')
        self.label_01['fg'] = ('White')
        self.label_01['pady'] = 15
        self.label_01.grid(row=0)

        self.user = Label(self.new_main_window, text='User')
        self.user['font'] = self.alternative_font
        self.user['bg'] = ('#005484')
        self.user['fg'] = ('White')
        self.user.grid(row=1, column=0)

        self.password = Label(self.new_main_window, text='Password')
        self.password['font'] = self.alternative_font
        self.password['bg'] = ('#005484')
        self.password['fg'] = ('White')
        self.password['pady'] = 10
        self.password.grid(row=2, column=0)

        self.entry_user = Entry(self.new_main_window)
        self.entry_user.grid(row=1, column=1)
        
        self.entry_pass = Entry(self.new_main_window)
        self.entry_pass['show'] = '*'
        self.entry_pass.grid(row=2, column=1)

        self.authenticator_button = Button(self.new_main_window, text='Authenticate', font=('Courier 10 Pitch', 12), activebackground='#005484', activeforeground='White')
        self.authenticator_button['bg'] = ('#005484')
        self.authenticator_button['command'] = self.authenticate
        self.authenticator_button['fg'] = ('White')
        self.authenticator_button.grid(row=3, column=1)

        self.message = Label(self.new_main_window, text='', font=('Courier 10 Pitch', 12))
        self.message['bg'] = ('#005484')
        self.message['pady'] = 15
        self.message.grid(row=3, column=2)

    def authenticate(self):
        connection = sq.connect('my_python_gui_database.db')

        main_cursor = connection.cursor()

        main_cursor.execute("SELECT * FROM database", 
        {
            'Username': str(self.entry_user.get()),
            'Password': str(self.entry_pass.get())
        })

        self.verify = main_cursor.fetchall()
        for i in self.verify:
            for verify in self.verify:
                print(str(verify[0]) + '\n' + str(verify[1]) + '\n')

        if str(self.entry_user.get()) in str(verify[0]) and str(self.entry_pass.get()) in verify[1]:
            self.message["text"] = "Authenticated"
            self.message['font'] = ('Courier 10 Pitch', 14)
            self.message['fg'] = ('White')
        else:
            self.message["text"] = "Athenticate Error"
            self.message['fg'] = ('Yellow')
            self.message['font'] = ('Courier 10 Pitch, Bold', 12)

        if str(self.entry_user.get()) in str(verify[0]) and str(self.entry_pass.get()) in verify[1]:
            self.enter_button_userspace = Button(self.new_main_window, text='User Space', font=('Courier 10 Pitch', 12), activebackground='#005484', activeforeground='White')
            self.enter_button_userspace['bg'] = ('#005484')
            self.enter_button_userspace['fg'] = ('White')
            self.enter_button_userspace['command'] = self.active_authenticate_button
            self.enter_button_userspace.grid(row=4, column=1)
        else:
            try:
                self.enter_button_userspace.destroy()
            except:
                print()

        self.entry_user.delete(0, END)
        self.entry_pass.delete(0, END)

    def active_button_02(self, master=None):
        self.new_main_window_02 = Toplevel()

        self.new_main_window_02.bind('<Control-l>', self.active_button)

        self.new_main_window_02.bind('<Control-i>', self.info_menu)

        self.new_main_window_02.bind('<Control-x>', quit)

        self.new_main_window_02.resizable(0, 0)

        self.main_window_02 = self.new_main_window_02.title('User Data')

        self.main_window_02 = self.new_main_window_02.geometry('700x400')

        self.main_window_02 = self.new_main_window_02.configure(bg='#005484')

        self.new_main_window_background_02 = PhotoImage(file='/home/esau_morais/Área de Trabalho/Python/My Python GUI/background.gif')

        self.new_main_window_label = Label(self.new_main_window_02, image=self.new_main_window_background_02)
        self.new_main_window_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.label_02 = Label(self.new_main_window_02, text='User Data'.center(15), font=('Chilanka', 28))
        self.label_02['bg'] = ('#005484')
        self.label_02['fg'] = ('White')
        self.label_02['pady'] = 15
        self.label_02.grid(row=0)

        self.username = Label(self.new_main_window_02, text='Username')
        self.username['font'] = self.alternative_font
        self.username['bg'] = ('#005484')
        self.username['fg'] = ('White')
        self.username['pady'] = 10
        self.username.grid(row=1, column=0)

        self.entry_username = Entry(self.new_main_window_02)
        self.entry_username.grid(row=1, column=1)

        self.password = Label(self.new_main_window_02, text='Password')
        self.password['font'] = self.alternative_font
        self.password['bg'] = ('#005484')
        self.password['fg'] = ('White')
        self.password['pady'] = 10
        self.password.grid(row=3, column=0)

        self.entry_password = Entry(self.new_main_window_02)
        self.entry_password.grid(row=3, column=1)
        self.entry_password['show'] = '*'

        self.authenticator_button_02 = Button(self.new_main_window_02, text='Save to Bank', font=('Courier 10 Pitch', 12), activebackground='#005484', activeforeground='White')
        self.authenticator_button_02['bg'] = ('#005484')
        self.authenticator_button_02['fg'] = ('White')
        self.authenticator_button_02['command'] = self.authenticate_02
        self.authenticator_button_02.grid(row=4, column=1)

    def authenticate_02(self):
        # Create database 'nd connect 

        connection = sq.connect('my_python_gui_database.db')

        main_cursor = connection.cursor()

        # Insert things to table

        main_cursor.execute("INSERT INTO database VALUES(:Username, :Password)",
        
        {
            'Username': self.entry_username.get(),
            'Password': self.entry_password.get()
        })

        connection.commit()

        self.message_02 = Label(self.new_main_window_02, activeforeground='White', font=('Courier 10 Pitch', 21))
        self.message_02['bg'] = ('#005484')
        self.message_02['fg'] = 'White'
        self.message_02.grid(row=4, column=2)

        if str(self.entry_username.get()) == '' or str(self.entry_password.get()) == '' or len(self.entry_password.get()) < 8:
            self.message_02['text'] = emojize(':warning:')
            self.message_02['fg'] = 'Yellow'

            main_cursor.execute("DELETE FROM database WHERE Username=?", (self.entry_username.get(),))

            main_cursor.execute("DELETE FROM database WHERE Password=?", (self.entry_password.get(),))

            main_cursor.fetchall()

            connection.commit()
        else:
            self.message_02['text'] = emojize(':heavy_check_mark:')
            self.message_02['fg'] = 'White'

            main_cursor.execute("SELECT * FROM database")

            connection.commit()

        self.entry_username.delete(0, END)
        self.entry_password.delete(0, END)

    def info_menu(self, master=None):
        self.info_window = Toplevel()

        self.info_window.bind('<Control-l>', self.active_button)

        self.info_window.bind('<Control-r>', self.active_button_02)

        self.info_window.bind('<Control-x>', quit)

        self.info_window.resizable(0, 0)

        self.info_title = self.info_window.title('Informations')

        self.info_geometry = self.info_window.geometry('700x400')

        self.info_background = self.info_window.configure(bg='#005484')

        self.info_image = PhotoImage(file='/home/esau_morais/Área de Trabalho/Python/My Python GUI/background.gif')

        self.info_background_01 = Label(self.info_window, image=self.info_image)
        self.info_background_01.place(x=0, y=0, relwidth=1, relheight=1)

        self.main_label_info = Label(self.info_window, text='My Python GUI Info', font=('Chilanka', 32), fg='White')
        self.main_label_info['bg'] = ('#005484')
        self.main_label_info['pady'] = 30
        self.main_label_info.pack(side=TOP)

        self.label_info_02 = Label(self.info_window, text='Software Developer → Esaú Morais\n Software Name → My Python GUI\n---------------------------------\n This software was created\n for user to quickly and easy\n into their particular account,\n creating other account\n and saving it on a database.', fg='White')
        self.label_info_02['bg'] = ('#005484')
        self.label_info_02['font'] = ('Courier 10 Pitch', 14)
        self.label_info_02.pack(side=TOP, pady=20)

    def help_menu(self):
        self.help_window = Toplevel()

        self.help_window.bind('<Control-l>', self.active_button)

        self.help_window.bind('<Control-r>', self.active_button_02)

        self.help_window.bind('<Control-i>', self.info_menu)

        self.help_window.bind('<Control-x>', quit)

        self.help_window.resizable(0, 0)

        self.help_title = self.help_window.title('Help me')

        self.help_geometry = self.help_window.geometry('700x400')

        self.help_background = self.help_window.configure(bg='#005484')

        self.help_image = PhotoImage(file='/home/esau_morais/Área de Trabalho/Python/My Python GUI/background.gif')

        self.help_background_02 = Label(self.help_window, image=self.help_image)
        self.help_background_02.place(x=0, y=0, relwidth=1, relheight=1)

        self.main_label_help = Label(self.help_window, text='My Python GUI Help', font=('Chilanka', 32))
        self.main_label_help['bg'] = ('#005484')
        self.main_label_help['fg'] = 'White'
        self.main_label_help['pady'] = 30
        self.main_label_help.pack(side=TOP)

        self.label_help_02 = Label(self.help_window, text='How can we help?')
        self.label_help_02['bg'] = ('#005484')
        self.label_help_02['fg'] = 'White'
        self.label_help_02['font'] = ('Courier 10 Pitch', 18)
        self.label_help_02['width'] = 18
        self.label_help_02['height'] = 2
        self.label_help_02.pack(side=TOP, pady=10)

        self.entry_help = Entry(self.help_window, state=DISABLED, disabledforeground='White')
        self.entry_help['width'] = 30
        self.entry_help.pack(side=TOP)

        self.button_enter_help = Button(self.help_window, text='Help me', font=('Courier 10 Pitch', 14), fg='White',
         activebackground='#005484', activeforeground='White', state=DISABLED, disabledforeground='White')
        self.button_enter_help['bg'] = ('#005484')
        self.button_enter_help['command'] = self.active_entry_help
        self.button_enter_help.pack(side=TOP, pady=20)

    def active_entry_help(self):
        pass
    
    def active_authenticate_button(self):

        authenticate_window = Toplevel()

        authenticate_window.resizable(0, 0)

        self.authenticate_title = authenticate_window.title('User Space')

        self.authenticate_geometry = authenticate_window.geometry('700x400')

        self.authenticate_image = PhotoImage(file='/home/esau_morais/Área de Trabalho/Python/My Python GUI/background.gif')

        self.authenticate_background = Label(authenticate_window, image=self.authenticate_image)
        self.authenticate_background.place(x=0, y=0, relwidth=1, relheight=1)

        self.authenticate_label = Label(authenticate_window, text='Welcome to User Sapace!', bg='#005484' ,fg='White', font=('Welcome', 72))
        self.authenticate_label.pack(pady=20)

window = Tk()

Functions(window)

window.mainloop()