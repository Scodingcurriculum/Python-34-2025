#Start code here
import datetime # your own code
start_date = datetime.date(2025, 5, 1)
end_date =  datetime.date(2025, 6,)
saturdays = 0
sundays = 0
while start_date < end_date:
  if start_date.weekday() == 5:
    saturdays += 1
  elif start_date.weekday() == 6:
    sundays += 1
  start_date += datetime.timedelta(days=1)
print(f"Saturdays = {saturdays}")
print(f"Sundays = {sundays}")
