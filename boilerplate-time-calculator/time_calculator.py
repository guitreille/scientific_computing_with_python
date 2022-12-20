from datetime import datetime, timedelta


def add_time(start, duration, dayOfWeek = None):
  # calculate end_dt
  start_dt = datetime.strptime(start, '%I:%M %p')
  duration = duration.split(':')
  end_dt = start_dt+timedelta(hours=int(duration[0]),minutes=int(duration[1]))

  # Add day and next days
  nb_days_later = (end_dt.date() - start_dt.date()).days
  end_dt_str = end_dt.time().strftime("%I:%M %p")
  end_dt_str += getEndWeekDay(dayOfWeek, nb_days_later) #will return '' if nothing given
  if nb_days_later == 1:
    end_dt_str += " (next day)"
    
  elif nb_days_later > 1:
    end_dt_str += f" ({nb_days_later} days later)"

  # strip if first char is a 0
  end_dt_str = end_dt_str.lstrip("0")
  return end_dt_str

def getEndWeekDay(begin_weekday_str, nb_days_later):
  if begin_weekday_str is None:
    return ''
  
  days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  pos = 0
  # find position in the list
  for day in days:
    if day.lower() == begin_weekday_str.lower():
      break
    pos += 1
  # return new position
  return ', ' + days[(pos + nb_days_later) % 7]