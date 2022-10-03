import datetime

dateInput = input()
try:
    dateStr = dateInput.split(".")
    date = datetime.datetime(int(dateStr[2]), int(dateStr[1]), int(dateStr[0]),0,0)
except ValueError:
    print('Дата введена неправильно')
    exit()
date1 = date+datetime.timedelta(days=10_000)
date2 = date+datetime.timedelta(minutes=1_000_000)
date3 = date+datetime.timedelta(seconds=1_000_000_000)
print(date1.year)
print(date2.year)
print(date3.year)