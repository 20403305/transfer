# How to Find the Current Day is Weekday or Weekends in Python

# Import Module
import datetime

# To Get the Week Number
weekNumber = datetime.datetime.today().weekday()

if weekNumber < 5:
    print("Today's DateTime is {0} and it's a Weekday".format(datetime.datetime.today()))
else:
    print ("Today's DateTime is {0} and it's a Weekend".format(datetime.datetime.today()))