# 3)Склонение слова
i = 1
procents = []  # создаем новый список
proc_val = ''  # создаем переменную для склонения слова "процент"
for i in range(100):  # наполняем список элементами от 1 до 100
    procents.append(i + 1)
for i, el in enumerate(procents):  # запускаем цикл "for", проверяем каждый элемент, присваеваем нужный падеж, выводим
    a = el % 10
    if a == 1 and el != 11:
        proc_val = 'процент'
        print(el, proc_val)
    if a == 2 or a == 3 or a == 4:
        proc_val = 'процента'
        print(el, proc_val)
    if el == 11 or a == 5 or a == 6 or a == 7 or a == 8 or a == 9 or a == 0:
        proc_val = 'процентов'
        print(el, proc_val)
