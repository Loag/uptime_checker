import sqlite3
from uptime_checker.models.link import link_obj
from uptime_checker.models.ping import ping_obj
from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception as err:
        return False

class DB:
  def __init__(self):
    self.connection = sqlite3.connect('uptime_checker.db', check_same_thread=False)
    self.cursor = self.connection.cursor()
    if not self.__check_table_exists():
      self.create_tables()

  def __check_table_exists(self):
    try:
      res = self.cursor.execute('SELECT name FROM sqlite_master WHERE type=table AND name in ("links", "pings");')
      if len(res) == 2:
        return True
      return False

    except sqlite3.Error as err:
      print(str(err))
      self.connection.rollback()
      return False

  def create_tables(self):
    try:
      # create links table
      self.cursor.execute('CREATE TABLE links(id integer PRIMARY KEY AUTOINCREMENT, link text, created_at text);')
      # create pings table
      self.cursor.execute('CREATE TABLE pings(id integer PRIMARY KEY AUTOINCREMENT, link_id integer, success text, elapsed text, created_at text);')
      
      self.connection.commit()
      return True
    except sqlite3.Error as err:
      print(str(err))
      self.connection.rollback()
      return False

  def get_links(self):
    try:
      return list(map(link_obj, self.cursor.execute(f'SELECT * FROM links').fetchall()))
    except sqlite3.Error as err:
      print(str(err))
      return []
  
  # return bool for success
  def create_link(self, link_data):
    try: 
      if is_valid_url(link_data[0]):
        self.cursor.execute(f'INSERT INTO links(link ,created_at) VALUES(?,?)', link_data)
        self.connection.commit()
        return True
      return False
    except sqlite3.Error as err:
      print(str(err))
      self.connection.rollback()
      return False

  def get_pings(self, link_id):
    try:
      return list(map(ping_obj, self.cursor.execute(f'SELECT * FROM pings WHERE link_id={link_id}').fetchall()))
    except sqlite3.Error as err:
      print(str(err))
      return []

  def create_pings(self, ping_data):
    try:
      self.cursor.executemany('INSERT INTO pings(link_id, success, elapsed, created_at) VALUES(?,?,?,?);',ping_data)
      self.connection.commit()
      return True
    except sqlite3.Error as err:
      print(str(err))
      self.connection.rollback()
      return False
