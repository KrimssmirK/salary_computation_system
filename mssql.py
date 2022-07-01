'''Microsoft SQL'''
import pymssql as MSSQLCnn

class UseDatabase:
  
  def __init__(self):
    self.config = {
      'host': '127.0.0.1',
      'user': 'SA',
      'password': 'G00t3r003',
      'database': 'time_records'
    }
    
  def __enter__(self):
    self.conn = MSSQLCnn.connect(**self.config)
    self.cursor = self.conn.cursor()
    return self.cursor
  
  def __exit__(self, exc_type, exc_value, exc_trace):
    self.conn.commit()
    self.cursor.close()
    self.conn.close() 