print('Введите строку')
data = input().strip().lower()
data = data[:1].upper()+data[1:len(data)]
print(data)
