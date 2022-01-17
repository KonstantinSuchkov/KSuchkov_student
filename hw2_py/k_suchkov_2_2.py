# 2. Дан список:
some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
new_list = []  # в этом списке кавычки перед и после чисел идут как отдельный элемент списка: '"', '05', '"'
result = []  # этот список я создал, чтобы после ''.join не было пробелов между кавычками: - в "05"...

for el in some_list:
    if el.isdigit(): # если el число, то добавляем 0, кавычки
        new_el = f'{int(el):02d}'
        new_el = ['"', new_el, '"']
        new_list.extend(new_el)
        new_el = ''.join(new_el)
        result.append(new_el)
    elif el[0] == '+': # если el начинается с плюса, то делаем тоже самое, только дополнительно ставим +
        new_el = f'+{int(el):02d}' # ничего красивее не придумал
        new_el = ['"', new_el, '"']
        new_list.extend(new_el)
        new_el = ''.join(new_el)
        result.append(new_el)
    else:
        new_list.append(el)
        result.append(el)

print(some_list)
print(new_list)
result = ' '.join(result)
print(result)
