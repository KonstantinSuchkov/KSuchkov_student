# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь, в котором
# ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы

def thesaurus(*args):
    names = {}  # создаем пустой словарь
    for item in args:
        key = item[0]  # ключ в словаре будет первой буквой имени
        if key not in names:  # если в словаре нет ключа, то добавляем его и список для имен
            names[key] = []
        names[key].append(item)
    return names


print(thesaurus("Ivan", "Petya", "Iliya", "Amelia", "Alex"))


# второй вариант по методичке с методом .setdefault
def thesaurus(*args):
    names = {}
    for item in args:
        names[item[0]] = names.setdefault(item[0], []) + [item]
    return names


print(thesaurus("Ivan", "Petya", "Iliya", "Amelia", "Alex"))
