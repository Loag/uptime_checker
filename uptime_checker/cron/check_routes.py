# get routes from db and try and get them all async
import grequests
from datetime import datetime
from threading import Thread
from time import sleep
from urllib.parse import urlparse

class Checker:
  def __init__(self, db, sleep_time=30):
    self.db = db
    self.running = False
    self.sleep_time = sleep_time

  def __get_all_links(self):
    return self.db.get_links()

  def __save_results(self, results):
    # needs to be a tuple

    def gen_obj(input):
      print(input[1].elapsed)
      return (
        input[0].id,
        str(input[1].ok),
        str(input[1].elapsed),
        datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
      )

    pings = list(map(gen_obj, results))
    return self.db.create_pings(pings)

  # iterate over all of the routes and check their uptime
  def __run(self):
    print("checking links now..")
    try:
      links = self.__get_all_links()
      res = grequests.map((grequests.get(u.link) for u in links))
      return  self.__save_results(zip(links, res))
    except Exception as err:
      print(err)
      return False
  
  def __run_loop(self):
    while self.running:
      self.__run()
      sleep(self.sleep_time)

  def start(self):
    self.running = True
    self.execution_thread = Thread(target=self.__run_loop, daemon=True)
    self.execution_thread.start()
  
  def stop(self):
    self.running = False

