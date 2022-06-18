import tkinter as tk
from tkinter import ttk
import re

class TimeEntry(ttk.Entry):
  
  def __init__(self, parent, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)
    self.error = tk.StringVar()
    self.configure(
      validate='focusout',
      validatecommand=(self.register(self._validate), '%P'),
      invalidcommand=(self.register(self._on_invalid), '%P')
    )
  
  def _validate(self, proposed):
    '''Regular Expression'''
    pattern = '[0-9]+:[0-9]+'
    if re.search(pattern, proposed) and len(proposed) < 6:
      return True
    return False
    

  def _on_invalid(self, proposed):
    self.error.set(
      f'{proposed} is invalid value'
    )