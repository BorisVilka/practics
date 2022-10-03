import math

print('Введите величину угла в градусах')
angle = float(input())*math.pi/180
sin = math.sin(angle)
cos = math.cos(angle)
tg = math.tan(angle)
print('Синус угла: ', sin)
print('Косинус угла: ', cos)
print('Тангенс угла: ', tg)

