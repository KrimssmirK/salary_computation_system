import tkinter as tk
from tkinter import ttk
from jsonvar import JSONVar
from time_in_out_form import TimeInOutForm

class TimeInOutApp(ttk.Frame):
  
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    
    '''data that holds the application'''
    self.jsonvar = JSONVar(self)
    
    '''components'''
    TimeInOutForm(self, self.jsonvar).grid()
    
    
    
    ''''''
    
    '''layout'''
    self.grid()
    
    
    ''''''