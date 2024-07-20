from tkinter import *
from tkinter import ttk

def init_screen():
    root = Tk()
    
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text='hello world').grid(column=0, row=0)
    ttk.Button(frm, text='Quit', command=root.destroy).grid(column=1, row=0)

    return root.mainloop()