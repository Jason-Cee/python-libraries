# Python Libraries

# Calculating Age
from datetime import datetime
year_born = int(input("Enter year born: "))
month_born = int(input("Enter your month born: "))
day_born = int(input("Enter your day born: "))

current_year = int(datetime.today().strftime("%Y"))
current_month = int(datetime.today().strftime("%m"))
current_day = int(datetime.today().strftime("%d"))

age = current_year - year_born - 1

if month_born < current_month:
    age += 1
elif current_month == month_born:
    if current_day >= day_born:
        age += 1

print(age)

# current time
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time = ", current_time)


# Task
import datetime
now = datetime.datetime.today()
print(now.year)
print(now.month)
print(now.day)
print(now.date())
myDate = now.date()
for i in range(14, 140, 14):
    print(myDate)
