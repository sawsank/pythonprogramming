import calendar
from datetime import datetime

given_date = datetime(2020, 7, 26)
weekday = calendar.day_name[given_date.weekday()]
print(weekday)