# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах

duration = 100000
# duration = int(input('Введите количество секунд: '))

if duration < 60:
    print(duration, 'сек')
elif 60 <= duration < 3600:
    m = duration // 60
    s = duration - (m * 60)
    print(m, 'мин', s, 'сек')
elif 3600 <= duration < 86400:
    h = duration // 3600
    m = (duration - (h * 3600)) // 60
    s = duration - (h * 3600) - (m * 60)
    print(h, 'час', m, 'мин', s, 'сек')
else:
    d = duration // 86400
    h = (duration - (d * 86400)) // 3600
    m = (duration - (d * 86400) - (h * 3600)) // 60
    s = duration - (d * 86400) - (h * 3600) - (m * 60)
    print(d, 'дн', h, 'час', m, 'мин', s, 'сек')
