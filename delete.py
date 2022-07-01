import tkinter as tk
from tkinter import ttk

# custom widgets
from labelinput import LabelInput
from mssql import UseDatabase

class Delete(ttk.Frame):
  def __init__(self, parent, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)
    
    # data of Edit
    self._vars = {
      'No': tk.StringVar()
    }
    
    # delete frame where the input widgets are in
    self.delete_frame = ttk.LabelFrame(self, text='Delete')
    self.delete_frame.grid(sticky=(tk.W + tk.E))
    
    LabelInput(
      self.delete_frame,
      'No',
      var = self._vars['No']
    ).grid()
    
    self.delete_button = ttk.Button(
      self.delete_frame, text='Delete', command=self._delete
    )
    self.delete_button.grid()
    
  def _delete(self):
    record_no = self._vars['No'].get()
    
    with UseDatabase() as cursor:
      SQL = f'DELETE FROM time_records WHERE record_no = {record_no}'
      cursor.execute(SQL)
    
    self._reset()
  
  def _reset(self):
    self._vars['No'].set('')
    
    