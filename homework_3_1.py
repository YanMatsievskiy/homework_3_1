'''Задача 1. Автомат с газировкой'''

x = float(input('Введите первоначальный объем газировки в автомате в литрах: '))
while x >= 0.2:
    print('OK')
    x -= 0.2
else:
    print('Error: lack of water')