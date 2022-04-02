# this is an event that the cron created
from uptime_checker.models.shared import try_parse_date, try_parse_delta

class Ping:
  def __init__(self, id, link_id, elapsed, created_at):
    self.id = id
    self.link_id = link_id
    self.elapsed = try_parse_delta(elapsed)
    self.created_at = try_parse_date(created_at)

  def to_dict(self):
    return {
      "id": self.id,
      "link_id":self.link_id,
      "elapsed":self.elapsed,
      "created_at":self.created_at
    }