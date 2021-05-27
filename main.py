# Python Libraries

# Exercise
# Ten dates 2 weeks apart
from datetime import datetime, timedelta

# Today's date
dt = datetime.now()
# Prints ten dates 14 days apart
for x in range(9):
    print(dt.strftime('%Y / %m \ %d'))
    dt = dt + timedelta(days=14 + 10)
