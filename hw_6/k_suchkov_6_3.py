# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что
# при хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл.
import pickle

users_len = 0
hobby_len = 0
file_1 = open('users.csv', 'r', encoding='utf-8')  # открываем файлы
file_2 = open('hobby.csv', 'r', encoding='utf-8')
users = file_1.read()  #
users = users.splitlines()  # создаем списки из данных файлов
hobby = file_2.read()
hobby = hobby.splitlines()
for i in range(len(users)):  # заносим длину списков в переменные
    users_len = i
for i in range(len(hobby)):
    hobby_len = i
if users_len > hobby_len:  # если список с фамилиями длиннее списка с хобби, то добавляем в хобби 'None'
    hobby.append('None')
if users_len < hobby_len:  # если список с хобби больше, списка с фамилиями, то выходим. Как выйти через код 1 не понял.
    exit()                 # т.е. я понимаю, что нужно, чтобы была ошибка или проблема, тогда будет код 1
# print(users)
# print(hobby)
result_data = dict(zip(users, hobby))  # объединяем списки в словарь через zip
print(result_data)
with open('6_3_dict.pkl', 'wb') as result_dict:  # сохраняем словарь в файл, используя pickle
    pickle.dump(result_data, result_dict)
with open('6_3_dict.pkl', 'rb') as result_dict:  # проверяем, печатаем результат
    result = pickle.load(result_dict)
print(result)
file_1.close()
file_2.close()
result_dict.close()
