print('Введите строку')
num = input().lower()
if len(num) != 6:
    print('Строка не может быть номером автомобиля')
    exit()
for i in {0, 1, 5}:
    if not 'a' <= num[i] <= 'z':
        print('Строка не может быть номером автомобиля')
        exit()
for i in range(2, 5):
    if not '0' <= num[i] <= '9':
        print('Строк1а не может быть номером автомобиля')
        exit()
