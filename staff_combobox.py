import tkinter as tk
from tkinter import ttk

class StaffCombobox(ttk.Combobox):
  
  def __init__(self, parent, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)
    self.error = tk.StringVar()
    self.configure(
      validate='focusout',
      validatecommand=(self.register(self._validate), '%P'),
      invalidcommand=(self.register(self._on_invalid), '%P')
    )
  
  def _validate(self, proposed):
    return proposed in ['Ishiah', 'Rj', 'Lhen', 'Fe']
  
  def _on_invalid(self, proposed):
    self.error.set(
      f'{proposed} is invalid value'
    )