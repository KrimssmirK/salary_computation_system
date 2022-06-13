import tkinter as tk
from tkinter import ttk
from labelinput import LabelInput

class TimeInOutForm(ttk.Frame):
  
  
  def __init__(self, parent, data_var, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)
    self.data_var = data_var
    
    self._vars = {
      'Staff': tk.StringVar(),
      'Time In': tk.StringVar(),
      'Time Out': tk.StringVar()
    }
    
    '''components'''
    LabelInput(
      self, 
      'Staff', 
      ttk.Combobox, 
      {
        'textvariable': self._vars['Staff'],
        'values': ['Ishiah', 'Rj', 'Lhen', 'Fe'] #temporary, this has to change from local to dynamically retrieving from the database.
      }
    ).grid()
    
    LabelInput(
      self,
      'Time In',
      ttk.Entry,
      {
        'textvariable': self._vars['Time In']
      }
    ).grid()
    
    LabelInput(
      self,
      'Time Out',
      ttk.Entry,
      {
        'textvariable': self._vars['Time Out']
      }
    ).grid()
    
    
    
    