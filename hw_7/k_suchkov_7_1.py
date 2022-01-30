# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#   |--settings
#   |--mainapp
#   |--adminapp
#   |--authapp

import os

dir_list = ('settings', 'mainapp', 'adminapp', 'authapp')  # создаем список с вложенными папками
for dir_1 in dir_list:  # создаем цикл, где каждое значения списка будет названием вложенной папки в папке me_project
    dir_path = os.path.join('my_project', dir_1)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)  # используем makedirs, тк будем создавать несколько папок
