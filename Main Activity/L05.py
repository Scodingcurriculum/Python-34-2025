#Start code here
import datetime # your own code
count = 0
start_date = datetime.date(2025,5,1)
end_date = datetime.date(2025,5,31)
while start_date < end_date:
  if start_date.weekday() < 5:
    count += 1
  start_date += datetime.timedelta(days=1)
#Additionally calculate the monthly wages if the daily wages are 2 # your own code
print(f"Weekdays = {count}")
daily_wages = 25
print(f"Monthly income for the month of May: {count * daily_wages} $")
