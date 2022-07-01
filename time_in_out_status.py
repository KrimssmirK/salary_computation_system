import tkinter as tk
from tkinter import ttk

class TimeInOutStatus(ttk.Frame):
  
  def __init__(self, parent, *args, **kwargs):
    super().__init__(parent, *args, **kwargs)
    
    self._records = dict()
    self._records_saved = 0
    
    self.status_frame = ttk.LabelFrame(self, text='Status')
    self.status_frame.grid(sticky=(tk.W + tk.E))
    for i in range(3):
      self.status_frame.columnconfigure(i, weight=1)
    
    ttk.Label(self.status_frame, text='Staff').grid(row=0, column=0, sticky=tk.W)
    ttk.Label(self.status_frame, text='Time In').grid(row=0, column=1, sticky=tk.W)
    ttk.Label(self.status_frame, text='Time Out').grid(row=0, column=2, sticky=tk.W)
    
    buttons = tk.Frame(self)
    buttons.grid(sticky=tk.W + tk.E, row=4)
    self.savebutton = ttk.Button(
      buttons, text='Save', command=self.master._on_save
    )
    self.savebutton.pack(side=tk.RIGHT)
       
  def add(self, data):
    no = self._is_data_exist(data)
    if no[0]:
      self._records[no[1]][1].config(text=data['Time In'])
      self._records[no[1]][2].config(text=data['Time Out'])
      return
    ADJUST = 1
    staff = tk.Label(self.status_frame, text=data['Staff'])
    staff.grid(row=self._records_saved + ADJUST, column=0, sticky=tk.W)
    time_in = tk.Label(self.status_frame, text=data['Time In'])
    time_in.grid(row=self._records_saved + ADJUST, column=1, sticky=tk.W)
    time_out = tk.Label(self.status_frame, text=data['Time Out'])
    time_out.grid(row=self._records_saved + ADJUST, column=2, sticky=tk.W)
    self._records[self._records_saved] = [staff, time_in, time_out]
    self._records_saved += 1
  
  def _is_data_exist(self, data):
    for _, _ in data.items():
      i = 0
      for var in self._records.values():
        temp = var
        print(temp)
        if var[0].cget('text') == data['Staff']:
          return True, i
        i += 1
    return False, 0
    