import tkinter as tk
from tkinter import ttk
from jsonvar import JSONVar

from datetime import datetime
from pathlib import Path
import csv

'''apps'''
from time_in_out_form import TimeInOutForm

class TimeInOutApp(ttk.Frame):
  
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    
    '''data that holds the application'''
    # self.jsonvar = JSONVar(self)
    
    '''components'''
    self.time_in_out_form = TimeInOutForm(self)
    self.time_in_out_form.grid()
    
    
    
    ''''''
    
    '''layout'''
    self.grid()
    
    
    ''''''
  
  def _on_save(self):
    datestring = datetime.today().strftime('%Y-%m-%d')
    filename = 'time_in_out_record_{}.csv'.format(datestring)
    newfile = not Path(filename).exists()

    try:
      data = self.time_in_out_form.get()
    except ValueError as e:
      print(str(e))
      return
    
    with open(filename, 'a', newline='') as fh:
      csvwriter = csv.DictWriter(fh, fieldnames=data.keys())
      if newfile:
        csvwriter.writeheader()
      csvwriter.writerow(data)

    