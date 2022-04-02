from uptime_checker.models.shared import try_parse_date

def link_obj(a):
  return Link(a[0], a[1], a[2])

class Link:
  def __init__(self, id, link, created_at):
    self.id = id
    self.link = link
    self.created_at = try_parse_date(created_at)

  def to_dict(self):
    return {
      "id": self.id,
      "link": self.link,
      "created_at": self.created_at
    }
