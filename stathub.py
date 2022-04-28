from tkinter import *


def stathubmain(a, y):
    stathub = Toplevel()
    stathub.title('StatHub 1.0')
    stathub.geometry("{0}x{1}+0+0".format(a, y))
    stathub.configure(bg='#DFD010')
    heading = Label(stathub, text='StatHub 1.0', bg='#DFD010', font=(99), fg='black')
    heading.pack(anchor='n')
    options_list = ["Option", "Option 2", "Option 3", "Option 4"]

    def goman(manager):
        manstats = LabelFrame(stathub, text='Manager Team', bg='#DFD010')
        manstats.pack()
        def clearman():
            manstats.pack_forget()
            single.pack_forget()
            clear_button.pack_forget()
        clear_button = Button(manstats, text='CLEAR', command=clearman, state=DISABLED, bg='#DFD010', padx=10, pady=10)
        clear_button.pack()
        single = Label(manstats, text=manager)
        single.pack()
        clear_button['state'] = NORMAL


    clicked = StringVar()
    clicked.set('Option 1')
    manstat = LabelFrame(stathub, text='Select Manager', bg='#DFD010')
    manstat.pack()
    manager_label = OptionMenu(manstat, clicked, *options_list)
    go_button = Button(manstat, text='GO', command=lambda: goman(clicked.get()), bg='#DFD010', padx=30, pady=10)

    manager_label.grid(row=0, column=0, padx=10, pady=10)
    go_button.grid(row=0, column=1, padx=10, pady=10)
