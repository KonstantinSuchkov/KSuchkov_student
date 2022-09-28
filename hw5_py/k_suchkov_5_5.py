# 5. Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список
# с сохранением порядка их следования в исходном списке
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
repeated_numbers = set()
result = set()
for numb in src:  # решение из урока
    if numb in repeated_numbers:
        continue
    if numb in result:
        result.discard(numb)
        repeated_numbers.add(numb)
        continue
    result.add(numb)
print([numb for numb in src if numb in result])

result = []
dublicate_numbs = []
for numb in src:  # еще одно решение
    count = 0  # количество повторений числа в списке
    for n in src:  # запускаем повторный цикл по списку
        if n == numb:  # если числа равняются, то добавляем +1 к количеству повторений
            count += 1
    if count == 1:  # если число повторяется только один раз, то добавляем его в результат
        result.append(numb)
print(result)
