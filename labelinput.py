'''compound widget'''
import tkinter as tk
from tkinter import ttk

'''custom library'''
from time_entry import TimeEntry



class LabelInput(ttk.Frame):
  """A label and input combined together"""
  
  def __init__(
    self, parent, label, var, input_class=TimeEntry, 
    input_args=None, label_args=None, *args, **kwargs
  ):
    super().__init__(parent, *args, **kwargs) # basic initialization of widgets
    input_args = input_args or {}
    label_args = label_args or {}
    self.variable = var
    self.variable.label_widget = self
    
    if input_class in (ttk.Checkbutton, ttk.Button):
      input_args['text'] = label
    else:
      self.label = ttk.Label(self, text=label, **label_args)
      self.label.grid(row=0, column=0, sticky=(tk.W + tk.E))
    
    if input_class in (
      ttk.Checkbutton, ttk.Button, ttk.Radiobutton
    ):
      input_args['variable'] = self.variable
    else:
      input_args['textvariable'] = self.variable
    
    if input_class == ttk.Radiobutton:
      self.input = tk.Frame(self)
      for v in input_args.pop('values', []):
        button = ttk.Radiobutton(
          self.input, value=v, text=v, **input_args
        )
        button.pack(
          side=tk.LEFT, ipadx=10, ipady=2, expand=True, fill='x'
        )
    else:
      self.input = input_class(self, **input_args)
      self.err_label = tk.Label(self, textvariable=self.input.error, fg='red')
      
    self.input.grid(row=1, column=0, sticky=(tk.W + tk.E))
    self.err_label.grid()
    self.columnconfigure(0, weight=1)
    
  def grid(self, sticky=(tk.E + tk.W), **kwargs):
    """Override grid to add default sticky values"""
    super().grid(sticky=sticky, **kwargs)
    
