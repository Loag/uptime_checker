from flask import Flask, jsonify, request, make_response
from datetime import datetime
from uptime_checker.models.shared import map_ser
from uptime_checker.db import DB

app = Flask(__name__)
db = DB()

@app.route('/', methods=['GET'])
def base():
  return "Uptime link checker"

# return list of links, each can be clicked
@app.route('/links', methods = ['GET']) 
def get_links():
  res = map_ser(db.get_links())
  return __makeres({"data": res})

# return pings for a link
@app.route('/links/<link_id>', methods=['GET'])
def get_link_pings(link_id):
  res = map_ser(db.get_pings(link_id))
  return __makeres({"data": res})

# create a new link to start pinging
@app.route('/links', methods = ['POST'])
def create_link():
  data = request.get_json(silent=True, force=True) 
  link = (data["link"], datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
  res = db.create_link(link)
  return __makeres({"status":res})

def __makeres(data):
    response = make_response(jsonify({"data": data}))
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response