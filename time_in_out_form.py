import tkinter as tk
from tkinter import ttk
from labelinput import LabelInput
from staff_combobox import StaffCombobox

class TimeInOutForm(ttk.Frame):
  
  
  def __init__(self, parent, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)
    
    self._vars = {
      'Staff': tk.StringVar(),
      'Time In': tk.StringVar(),
      'Time Out': tk.StringVar()
    }
    
    self.time_record_frame = ttk.LabelFrame(self, text='Time Record')
    self.time_record_frame.grid(sticky=(tk.W + tk.E))
    
    '''components'''
    LabelInput(
      self.time_record_frame, 
      'Staff', 
      input_class=StaffCombobox, #ttk.Combobox 
      var = self._vars['Staff'],
      #temporary, this has to change from local to dynamically retrieving from the database.
      input_args =  {'values': ['Ishiah', 'Rj', 'Lhen', 'Fe']}
    ).grid()
    
    LabelInput(
      self.time_record_frame,
      'Time In',
      var = self._vars['Time In']
    ).grid()
    
    LabelInput(
      self.time_record_frame,
      'Time Out',
      var = self._vars['Time Out']
    ).grid()
    
    buttons = tk.Frame(self.time_record_frame)
    buttons.grid(sticky=tk.W + tk.E, row=4)
    self.addbutton = ttk.Button(
      buttons, text='Add', command=self.master._on_add
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
