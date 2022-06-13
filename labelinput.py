'''compound widget'''
from tkinter import ttk

class LabelInput(ttk.Frame):
  """A label and input combined together"""
  
  def __init__(self, parent, label, inp_cls, inp_args, *args, **kwargs):
    super().__init__(parent, *args, **kwargs) # basic initialization of widgets
    
    self.label = ttk.Label(self, text=label)
    self.input = inp_cls(self, **inp_args)
    
    self.label.pack()
    self.input.pack()