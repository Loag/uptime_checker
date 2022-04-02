from datetime import datetime

DATE_TIME_FMT = "%m/%d/%Y, %H:%M:%S"
DELTA_FMT = "" # need to think about this

# try to convert from string or fail if it can't
def try_parse_dt(format_str, dt_time_str):
  try:
    return datetime.strptime(dt_time_str, format_str)
  except Exception as err:
    print(f"failed to parse time with err: {err}")
    raise RuntimeError from err

def try_parse_date(date):
  return try_parse_dt(DATE_TIME_FMT, date)

def try_parse_delta(delta):
  return try_parse_dt(DELTA_FMT, delta)