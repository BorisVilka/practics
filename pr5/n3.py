print('Введите строку')
inp1 = input()
print('Введите строку')
inp2 = input()
while True:
    ind1 = inp1.find(inp2)
    if ind1 == -1:
        break
    ind2 = inp1.find(inp2, ind1 + len(inp2))
    if ind2 != -1:
        inp1 = inp1.replace(inp2, '', 1)
    else:
        break
print('Первая строка после удаления всех вхождений второй, кроме последнего: ', inp1)
