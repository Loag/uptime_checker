from uptime_checker.models.shared import try_parse_date

class Link:
  def __init__(self, id, link, created_at):
    self.id = id
    self.link = link
    self.created_at = try_parse_date(created_at)

  def __to_dict__(self):
    return {
      "id": self.id,
      "link": self.link,
      "created_at": self.created_at
    }
