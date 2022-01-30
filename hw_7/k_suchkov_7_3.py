# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates

import os
import shutil

folder = []

for top, dirs, files in os.walk('my_project'):  # проходим по папке my_project и наполняем список путями к файлам
    for name in files:
        folder.append(os.path.join(top, name))
for el in folder:  # теперь идем по списку и если элемент заканчивается на .html, то создаем директория и копируем файл
    if el.endswith('.html'):
        path_for_dir = el.split('\\')
        dir_path = os.path.join('templates', os.path.join(path_for_dir[1], path_for_dir[2]))  # так и не додумал
        if not os.path.exists(dir_path):  # как сделать универсальнее, например, если файл в трех папках-матрешках
            os.makedirs(dir_path)
        shutil.copyfile(el, f'{dir_path}/{path_for_dir[-1]}')
