import random

n = random.randint(4, 30)
print('Игра началась')
while n >= 1:
    print(f'Осталось {n} камней, введите число камней, которые нужно убрать из кучи, моэно выбрать от 1 до 3 камней')
    delta = int(input())
    n -= min(3, delta)
    if n <= 1:
        print('Вы выиграли!')
        break
    n -= random.randint(1, 3)
    if n <= 1:
        print('Вы проиграли')
print('Игра закончена')
