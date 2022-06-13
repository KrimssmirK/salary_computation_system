import tkinter as tk
from labelinput import LabelInput
from tkinter import ttk
from jsonvar import JSONVar

variables = dict()

root = tk.Tk()

staff = ['ishiah', 'lhen', 'rj', 'fe']
variables['Staff'] = tk.StringVar()
LabelInput(
  root, 'Staff', ttk.Combobox, {'textvariable': variables['Staff'], 'values': staff}
).pack()

var1 = JSONVar(root)
var1.set('kenji')
var2 = JSONVar(root, value={'a': 10, 'b': 15})

print('Var1: ', var1.get()[1])

print('Var2: ', var2.get()['b'])

root.mainloop()