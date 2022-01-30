# 2. * (вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта

import os


def make_dir(path_root, name_obj):  # сделал функцию, чтобы сократить и без того длинный код
    dir_path = os.path.join(path_root, name_obj[1].strip())
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


with open('config.yaml', 'r', encoding='utf-8') as file_1:
    for el in file_1.readlines():
        el_name = el.split('|--')  # создаем переменную для наименования папок и файлов
        if el_name[1].find('.') < 0 and el.find('   |') < 0:  # условия для нахождения главной папки - my_project
            main_root = os.path.join(el_name[1].strip())
            if not os.path.exists(main_root):
                os.makedirs(main_root)
        elif el_name[1].find('.') < 0 and el.find('   |--') == 0:  # условия для папок, входящих в главную папку
            root_2 = el_name[1].strip()
            path = f'{main_root}\\{root_2}'  # запоминаем путь для записи файлов
            make_dir(main_root, el_name)
        elif el_name[1].find('.') < 0 and el.find('   |  |--') == 0:  # условия для следующего уровня папок
            root_3 = el_name[1].strip()
            path = f'{main_root}\\{root_2}'  # запоминаем путь
            make_dir(path, el_name)
        elif el_name[1].find('.') < 0 and el.find('   |     |--') == 0:  # условия для следующего уровня папок
            root_4 = el_name[1].strip()
            path = f'{main_root}\\{root_2}\\{root_3}'  # запоминаем путь
            make_dir(path, el_name)
        else:  # если элемент не папка, а файл, то создаем его в соответствующей директории
            file_name = el_name[1].strip()
            path_for_file = f'{path}\\{file_name}'
            make_file = open(path_for_file, 'w')
