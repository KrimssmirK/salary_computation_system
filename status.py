import tkinter as tk
from tkinter import ttk

# custom widgets
from mssql import UseDatabase

class Status(ttk.Frame):
  
  def __init__(self, parent, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)
    
    self._records = []
    
    self.status_frame = ttk.LabelFrame(self, text='Status')
    self.status_frame.grid(sticky=(tk.W + tk.E))
    COLUMNS = 5
    for i in range(COLUMNS):
      self.status_frame.columnconfigure(i, weight=1)
    
    ttk.Label(self.status_frame, text='No').grid(row=0, column=0, sticky=tk.W)
    ttk.Label(self.status_frame, text='Staff').grid(row=0, column=1, sticky=tk.W)
    ttk.Label(self.status_frame, text='Date').grid(row=0, column=2, sticky=tk.W)
    ttk.Label(self.status_frame, text='Time In').grid(row=0, column=3, sticky=tk.W)
    ttk.Label(self.status_frame, text='Time Out').grid(row=0, column=4, sticky=tk.W)
    
    self._refresh()

    self.refresh_button = ttk.Button(
      self, text='Refresh', command=self._refresh
    )
    self.refresh_button.grid()
    
  
  def _refresh(self):
    self._reset()
    
    with UseDatabase() as cursor:
      SQL = 'SELECT * FROM time_records;'
      cursor.execute(SQL)
      self._data = cursor.fetchall()
    
    print(self._data)
    
    current_row = 1
    for data in self._data:
      current_column = 0
      for value in data:
        new_label = ttk.Label(self.status_frame, text=value)
        new_label.grid(row=current_row, column=current_column, sticky=tk.W)
        self._records.append(new_label)
        current_column += 1
      current_row += 1
  
  def _reset(self):
    for record in self._records:
      record.destroy()
    
    
       


  

    