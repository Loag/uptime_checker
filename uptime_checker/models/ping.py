# this is an event that the cron created
from uptime_checker.models.shared import try_parse_date, try_parse_delta

def ping_obj(a):
  return Ping(a[0], a[1], a[2], a[3], a[4])

class Ping:
  def __init__(self, id, link_id, success, elapsed, created_at):
    self.id = id
    self.link_id = link_id
    self.success = success
    self.elapsed = try_parse_delta(elapsed).microsecond
    self.created_at = try_parse_date(created_at)

  def to_dict(self):
    return {
      "id": self.id,
      "link_id":self.link_id,
      "success": self.success,
      "elapsed":self.elapsed,
      "created_at":self.created_at
    }