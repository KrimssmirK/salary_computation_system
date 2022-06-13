'''main program of salary computation system'''

'''Tkinter'''
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from pathlib import Path
import csv
import pymssql as MSSQLCnn
from mssql import UseDatabase

'''global variable'''
variables = dict()
current_data = dict()
current_row = 1

root = tk.Tk()
root.title('Salary Computation System')
root.eval('tk::PlaceWindow . center')
root.resizable(False, False)

time_frame = ttk.Frame(root)
time_frame.grid(row=0, column=0, sticky=tk.N, padx=10, pady=10)
'''
LEFT component 1 - staff names
'''
staff = ['ishiah', 'lhen', 'rj', 'fe']
variables['Staff'] = tk.StringVar()
ttk.Label(
  time_frame, text='Staff'
).pack()
ttk.Combobox(
  time_frame, textvariable=variables['Staff'], values=staff
).pack()

'''
LEFT component 2 - time in
'''
variables['Time In'] = tk.StringVar()
ttk.Label(
  time_frame, text='Time In'
).pack()
ttk.Entry(
  time_frame, textvariable=variables['Time In']
).pack()

'''
LEFT component 3 - time out
'''
variables['Time Out'] = tk.StringVar()
ttk.Label(
  time_frame, text='Time Out'
).pack()
ttk.Entry(
  time_frame, textvariable=variables['Time Out']
).pack()

'''
LEFT component 4 - reset and save buttons
'''
reset_add_buttons = ttk.Frame(time_frame)
reset_button = ttk.Button(reset_add_buttons, text='Reset')
add_button = ttk.Button(reset_add_buttons, text='Add')
reset_button.grid(row=0, column=0)
add_button.grid(row=0, column=1)
reset_add_buttons.pack(padx=10, pady=10)

'''
RIGHT component 1 - status
'''
status_frame = ttk.Frame(root)
status_frame.grid(row=0, column=1, sticky=tk.N, padx=10, pady=10)

status = ttk.LabelFrame(status_frame, text='Status')
status.pack()
ttk.Label(status, text='Staff').grid(row=0, column=0, ipadx=50)
ttk.Label(status, text='Time In').grid(row=0, column=1, ipadx=10)
ttk.Label(status, text='Time Out').grid(row=0, column=2, ipadx=10)

'''
save button
'''
save_button = ttk.Button(root, text='Save')
save_button.grid(row=1, column=1, sticky=tk.E, padx=10, pady=20)

def on_reset():
  for variable in variables.values():
    if isinstance(variable, tk.BooleanVar):
      variable.set(False)
    else:
      variable.set('')

reset_button.configure(command=on_reset)


def on_add():
  '''check if there is none in input'''
  for variable in variables.values():
    if variable.get() == '':
      print('there is a missing input')
      return
  global current_row, current_data
  data = dict()
  for key, variable in variables.items():
    try:
      data[key] = variable.get()
    except tk.TclError:
      print(f'Error in field: {key}. Data was not saved!')
      return
  ttk.Label(status, text=data['Staff']).grid(row=current_row, column=0, ipadx=50)
  ttk.Label(status, text=data['Time In']).grid(row=current_row, column=1, ipadx=10)
  ttk.Label(status, text=data['Time Out']).grid(row=current_row, column=2, ipadx=10)
  current_data[current_row] = data
  current_row += 1
  
  on_reset()

add_button.configure(command=on_add)

def on_save():
  """add to database"""
  global current_data
#   for data in current_data.values():
#     print(data)
  
  datestring = datetime.today().strftime('%Y-%m-%d')
  filename = f'time_record{datestring}.csv'
  newfile = not Path(filename).exists()
  
  with open(filename, 'a', newline='') as fh:
    csvwriter = csv.DictWriter(fh, fieldnames={'Staff': '', 'Time In': '', 'Time Out': ''}.keys())
    if newfile:
      csvwriter.writeheader
    for data in current_data.values():
      csvwriter.writerow(data)

def test_db():
  # MSSQLdb = MSSQLCnn.connect(
  #   '127.0.0.1',
  #   'SA',
  #   'G00t3r003',
  #   'time_records'
  # )
  # mySQLcursor = MSSQLdb.cursor()
  
  # SQL = 'SELECT * FROM time_records;'
  # mySQLcursor.execute(SQL)
  # mySQLresult = mySQLcursor.fetchone()
  
  # if mySQLresult is None:
  #   print('mssql connection error')
  # else:
  #   print('mssql connection SUCCESS')
  #   print(mySQLresult)
  
  # MSSQLdb.close()
  # mySQLcursor.close()
  dbconfig = {
    'host': '127.0.0.1',
    'user': 'SA',
    'password': 'G00t3r003',
    'database': 'time_records'
  }
  
  with UseDatabase(dbconfig) as cursor:
    SQL = 'SELECT * FROM time_records;'
    cursor.execute(SQL)
    result = cursor.fetchone()
    print(result)

save_button.configure(command=test_db)


root.mainloop()