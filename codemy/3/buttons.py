#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#+ Autor:  	Ran#
#+ Creado: 	2023/03/25 14:04:55.708225
#+ Editado:	2023/03/25 14:17:58.139739
# ------------------------------------------------------------------------------
from tkinter import *
# ------------------------------------------------------------------------------


# ------------------------------------------------------------------------------
root = Tk()

def on_click():
    lbl = Label(root, text='Button clicked')
    lbl.pack()

# you can also use hex color codes
btn = Button(root, text='Click me!', padx='50', pady='50', command=on_click, fg="yellow", bg="red")
btn.pack()

root.mainloop()
# ------------------------------------------------------------------------------
