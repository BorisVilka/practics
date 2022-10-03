import datetime

print('Введите даты отправления и прибытия поезда в формате ДД.ММ.ГГГГ ММ:ЧЧ, каждое в отдельной строке')
dateInput1 = input().split(" ")
dateStr1 = dateInput1[0].split(".")
timeStr1 = dateInput1[1].split(":")
dateInput2 = input().split(" ")
dateStr2 = dateInput2[0].split(".")
timeStr2 = dateInput2[1].split(":")
date1 = datetime.datetime(int(dateStr1[2]), int(dateStr1[1]), int(dateStr1[0]), int(timeStr1[0]), int(timeStr1[1]))
date2 = datetime.datetime(int(dateStr2[2]), int(dateStr2[1]), int(dateStr2[0]), int(timeStr2[0]), int(timeStr2[1]))
ans = date2 - date1
print('Дней в пути: ',ans)
