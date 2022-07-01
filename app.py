'''the main program to be executed'''

import tkinter as tk

# custom widgets
from time_record import TimeRecord
from status import Status
from edit import Edit
from delete import Delete
from mssql import UseDatabase

class Application(tk.Tk):
  
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.title('Salary Computation System')
    self.eval('tk::PlaceWindow . center')
    self.resizable(False, False)
    
    Status(self).grid(padx=100, pady=10)
    TimeRecord(self).grid(padx=100, pady=10)
    Edit(self).grid(padx=100, pady=10)
    Delete(self).grid(padx=100, pady=10)

if __name__ == '__main__':
  app = Application()
  app.mainloop()