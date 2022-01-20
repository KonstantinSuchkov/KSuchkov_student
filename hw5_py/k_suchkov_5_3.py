# 3. Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В') ...

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Амелия', 'Варвара'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б'
]


def school(names, class_numb):
    for i in range(0, len(names)):
        if len(names) > len(class_numb):
            class_numb.append('None')
        var = (names[i], class_numb[i])
        yield var


result = school(tutors, klasses)
print(type(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
print(next(result))
