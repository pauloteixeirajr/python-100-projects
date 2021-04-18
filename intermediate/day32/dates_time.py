# Working with dates and times
import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
hours = now.hour
day_of_week = now.weekday()

# Creating new datetime object
date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=18, minute=30)
print(date_of_birth)
