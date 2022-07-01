import tkinter as tk
from tkinter import ttk

# custom widgets
from labelinput import LabelInput
from mssql import UseDatabase

class TimeRecord(ttk.Frame):
  
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    
    self._vars = {
      'Staff': tk.StringVar(),
      'Date': tk.StringVar(),
      'Time In': tk.StringVar(),
      'Time Out': tk.StringVar()
    }
    
    self.time_record_frame = ttk.LabelFrame(self, text='Time Record')
    self.time_record_frame.grid(sticky=(tk.W + tk.E))
    
    LabelInput(
      self.time_record_frame,
      'Staff',
      var = self._vars['Staff']
    ).grid()
    
    LabelInput(
      self.time_record_frame,
      'Date',
      var = self._vars['Date']
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
      buttons, text='Add', command=self._add
    )
    self.addbutton.pack(side=tk.RIGHT)
    
  
  def _add(self):
    staff = self._vars['Staff'].get()
    date = self._vars['Date'].get()
    time_in = self._vars['Time In'].get()
    time_out = self._vars['Time Out'].get()
    
    with UseDatabase() as cursor:
      SQL = f"INSERT INTO time_records (staff, date_in, time_in, time_out) VALUES ('{staff}', '{date}', '{time_in}', '{time_out}');"
      cursor.execute(SQL)
    
    self._reset()
  
  def _reset(self):
    for variable in self._vars.values():
      variable.set('')

    