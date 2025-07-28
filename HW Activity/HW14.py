#Start code here
import math
print("========FINDING THE REVOLUTION TIME IN EARTH YEARS=========")
print("Choose a planet: - ")
print("1. Mercury")
print("2. Venus")
print("3. Mars")
print("4. Jupiter")
print("=======================================")
ch = int(input("Enter your choice: - "))
Earth_years = ""
year_span = 1
if ch == 1:
  # Year span is the time that planet takes to complete 1 revolution # your own code
  #Just like the Earth takes 365 days, Mercury takes 88 Earth days to complete 1 revolution # your own code
  #Formula:   How many Earth years a planet takes to complete a revolution =  year_span / 365 # your own code
  year_span = 88
  Earth_years = year_span / 365
  print(f"Mercury takes {Earth_years} years to complete 1 revolution.")
elif ch == 2:
  #Just like the Earth takes 365 days, Venus takes 225 Earth days to complete 1 revolution # your own code
  year_span = 225
  Earth_years = year_span / 365
  print(f"Venus takes {Earth_years} years to complete 1 revolution.")
elif ch == 3:
  #Just like the Earth takes 365 days, Mars takes 687 Earth days to complete 1 revolution # your own code
  year_span = 687
  Earth_years = year_span / 365
  print(f"Mars takes {Earth_years} years to complete 1 revolution.")
elif ch == 4:
  #Just like the Earth takes 365 days, Jupiter takes 4333 Earth days to complete 1 revolution # your own code
  year_span = 4333
  Earth_years = year_span / 365
  print(f"Jupiter takes  {Earth_years} years to complete 1 revolution.")
else:
  print("Invalid choice!!")
