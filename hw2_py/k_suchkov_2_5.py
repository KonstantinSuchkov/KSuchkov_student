# 5. Создать список, содержащий цены на товары
prices = [57.9, 46.51, 97, 33.82, 44.04, 87.23, 21.08, 26.06, 35, 20.04, 7.40, 0.55]
print(prices)
for i in prices: # выводим список одной строкой согласно заданию в формате " -- руб -- коп "
    rub = int(i)
    cop = int(i*100%100)
    print(f'{rub:02d} руб {cop:02d} коп', end=',')
    if i == prices[-1]:
        print(f'{rub:02d} руб {cop:02d} коп')

for i in sorted(prices.copy()): # выводим список по возрсатанию цены, используем .copy, чтобы не менять сам список
    rub = int(i)
    cop = int(i*100%100)
    print(f'{rub:02d} руб {cop:02d} коп', end=',')
    if i == sorted(prices.copy())[-1]:
        print(f'{rub:02d} руб {cop:02d} коп')

print(prices) # проверяем, что основной список не поменялся

new_prices = sorted(prices.copy())[::-1] # создаем новый список по убыванию, используем "реверс" ::-1 (стр. 8 методички)
for i in new_prices:
    rub = int(i)
    cop = int(i*100%100)
    print(f'{rub:02d} руб {cop:02d} коп', end=',')
    if i == new_prices[-1]:
        print(f'{rub:02d} руб {cop:02d} коп')

for i in sorted(prices)[-5:]: # сортируем список по возрастанию и отбираем 5 последних чисел
    print(f'{int(i):02d} руб {int(i*100%100):02d} коп', end=',')


