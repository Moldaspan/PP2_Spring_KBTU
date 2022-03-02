from datetime import datetime, timedelta
#1)
start_date = datetime.now().date()
end_date = datetime.now().date() - timedelta(days=5)
print(end_date.strftime("%x"))

print('-' * 30)

#2)
print('Yesterday', datetime.now() -timedelta(days = 1))
print('Today', datetime.now())
print('Tomorrow', datetime.now() +  timedelta(days = 1))

print('-' * 30)

#3)
dt = datetime.today().replace(microsecond=0)
print(dt)

print('-' * 30)

#4)
date1 = datetime.now()
date2 = datetime(2021, 12, 31, 23, 59, 59)
difference = date1 - date2
print(difference. total_seconds())
