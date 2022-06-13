'''the main program to be executed'''

import tkinter as tk
# from jsonvar import JSONVar
from time_in_out_app import TimeInOutApp

class Application(tk.Tk):
  
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    
    '''data that holds the application'''
    # self.jsonvar = JSONVar(self)
    
    
    
    
    
    
    '''Apps'''
    #1
    TimeInOutApp(self).grid()
    
    #2
    
    #3
    ''''''''''''''''''''''''''''''''''''
    
    
    
    
    '''layout of the application'''
    self.title('Salary Computation System')
    self.eval('tk::PlaceWindow . center')
    self.resizable(False, False)
    ''''''''''''''''''''''''''''''''''''

if __name__ == '__main__':
  app = Application()
  app.mainloop()