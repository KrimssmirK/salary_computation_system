import tkinter as tk
from tkinter import ttk

# custom widgets
from labelinput import LabelInput
from mssql import UseDatabase

class Edit(ttk.Frame):
  
  def __init__(self, parent, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)
    
    # data of Edit
    self._vars = {
      'No': tk.StringVar(),
      'Staff': tk.StringVar(),
      'Date': tk.StringVar(),
      'Time In': tk.StringVar(),
      'Time Out': tk.StringVar()
    }
    
    # edit frame where the input widgets are in
    self.edit_frame = ttk.LabelFrame(self, text='Edit')
    self.edit_frame.grid(sticky=(tk.W + tk.E))
    
    LabelInput(
      self.edit_frame,
      'No',
      var = self._vars['No']
    ).grid()
    
    self.search_button = ttk.Button(
      self.edit_frame, text='Search', command=self._search
    )
    self.search_button.grid()
    
    LabelInput(
      self.edit_frame,
      'Staff',
      var = self._vars['Staff']
    ).grid()
    
    LabelInput(
      self.edit_frame,
      'Date',
      var = self._vars['Date']
    ).grid()
    
    LabelInput(
      self.edit_frame,
      'Time In',
      var = self._vars['Time In']
    ).grid()
    
    LabelInput(
      self.edit_frame,
      'Time Out',
      var = self._vars['Time Out']
    ).grid()
    
    self.update_button = ttk.Button(
      self.edit_frame, text='Update', command=self._update
    )
    self.update_button.grid()
    


  def _search(self):
    record_no = self._vars['No'].get()
    
    with UseDatabase() as cursor:
      SQL = f"SELECT * FROM time_records where record_no = '{record_no}';"
      cursor.execute(SQL)
      result = cursor.fetchall()
    
    staff = result[0][1]
    date = result[0][2]
    time_in = result[0][3]
    time_out = result[0][4]
    
    self._vars['Staff'].set(staff)
    self._vars['Date'].set(date)
    self._vars['Time In'].set(time_in)
    self._vars['Time Out'].set(time_out)


  def _update(self):
    record_no = self._vars['No'].get()
    staff = self._vars['Staff'].get()
    date = self._vars['Date'].get()
    time_in = self._vars['Time In'].get()
    time_out = self._vars['Time Out'].get()
    
    with UseDatabase() as cursor:
      SQL = f"UPDATE time_records SET staff = '{staff}', date_in = '{date}', time_in = '{time_in}', time_out = '{time_out}' WHERE record_no = {record_no};"
      cursor.execute(SQL)
    
    self._reset()
    
  def _reset(self):
    for variable in self._vars.values():
      variable.set('')
    