import datetime

print('Введите дату рождения в формате ДД.ММ.ГГГГ')
dateInput = input()
try:
    dateStr = dateInput.split(".")
    date = datetime.datetime(int(dateStr[2]), int(dateStr[1]), int(dateStr[0]), 0, 0)
except ValueError:
    print('Дата введена неправильно')
    exit()
date1 = date + datetime.timedelta(days=10_000)
date2 = date + datetime.timedelta(minutes=1_000_000)
date3 = date + datetime.timedelta(seconds=1_000_000_000)
print('10 000 дней исполнится ', date1.day, '.', date1.month, '.', date1.year)
print('1 000 000 минут исполнится ', date2.day, '.', date2.month, '.', date2.year)
print('1 000 000 000 секунд исполнится ', date3.day, '.', date3.month, '.', date3.year)
