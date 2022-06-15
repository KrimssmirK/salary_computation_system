import tkinter as tk
from tkinter import ttk
from labelinput import LabelInput

class TimeInOutForm(ttk.Frame):
  
  
  def __init__(self, parent, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)
    
    self._vars = {
      'Staff': tk.StringVar(),
      'Time In': tk.StringVar(),
      'Time Out': tk.StringVar()
    }
    
    '''components'''
    LabelInput(
      self, 
      'Staff', 
      input_class=ttk.Combobox, 
      var = self._vars['Staff'],
      #temporary, this has to change from local to dynamically retrieving from the database.
      input_args =  {'values': ['Ishiah', 'Rj', 'Lhen', 'Fe']}
    ).grid()
    
    LabelInput(
      self,
      'Time In',
      var = self._vars['Time In']
    ).grid()
    
    LabelInput(
      self,
      'Time Out',
      var = self._vars['Time Out']
    ).grid()
    
    buttons = tk.Frame(self)
    buttons.grid(sticky=tk.W + tk.E, row=4)
    self.addbutton = ttk.Button(
      buttons, text='Add', command=None
    )
    self.addbutton.pack(side=tk.RIGHT)
    
    self.resetbutton = ttk.Button(
      buttons, text='Reset', command=self.reset
    )
    self.resetbutton.pack(side=tk.RIGHT)    
  
  def reset(self):
    for var in self._vars.values():
      if isinstance(var, tk.BooleanVar):
        var.set(False)
      else:
        var.set('')
  
  def get(self):
    data = dict()
    for key, variable in self._vars.items():
      try:
        data[key] = variable.get()
      except tk.TclError:
        message = f'Error in field: {key}. Data was not saved!'
        raise ValueError(message)
    return data
