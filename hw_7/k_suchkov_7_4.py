# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
# размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках),
# размер которых не превышает этой границы, но больше предыдущей (начинаем с 0)
import os

result_stat = {
    0: 0,
    100: 0,
    1000: 0,
    10000: 0,
    100000: 0
}
for root, dirs, files in os.walk('some_data'):
    for file in files:
        size = os.stat(os.path.join(root, file)).st_size
        if size < 100:
            result_stat[100] += 1
        elif size < 1000:
            result_stat[1000] += 1
        elif size < 10000:
            result_stat[10000] += 1
        elif size < 100000:
            result_stat[100000] += 1
        elif size == 0:
            result_stat[0] += 1

print(result_stat)
