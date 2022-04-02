from uptime_checker.app import app
from uptime_checker.cron.check_routes import Checker
from uptime_checker.db import DB

def run():
    db = DB()
    checker = Checker(db)
    checker.start()
    app.run()