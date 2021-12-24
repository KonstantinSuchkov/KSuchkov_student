# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000...
# возможно слишком много переменных((
el = 0
n = 1
old_el = 0
my_list = [n]
result_1 = 0  # первая сумма чисел
result_2 = 0  # вторая сумма чисел, после выполнения +17

while True:
    n += 1
    sum_number = 0
    if n % 2 != 0:  # наполняем список элементами - нечетные числа в кубе ( **3)
        el = n ** 3
        my_list.append(el)
        old_el = el
        continue
    while el != 0:  # считаем сумма цифр в каждом числе
        sum_number = sum_number + el % 10
        el = el // 10
    if sum_number % 7 == 0:
        result_1 += old_el  # суммы цифр, делящиеся на 7 без остатка, складываются в result1
    if n > 1000:  # после получения первого результата, когда цикл доходит до n 1000, добавляем 17 к каждому элементу
        my_list = [n + 17 for n in my_list]
        for n in my_list:  # повторно считаем суммы цифр и складываем их, если делятся на 7 без остатка
            old_el = n
            el = n
            sum_number = 0
            while el != 0:
                sum_number = sum_number + el % 10
                el = el // 10
            if sum_number % 7 == 0:
                result_2 += old_el
        break

print(result_1)
print(result_2)
