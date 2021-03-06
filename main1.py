# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration
# в секундах: до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек;
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
#Примеры:

# duration = 53
# 53 сек
# duration = 153
# 2 мин 33 сек
# duration = 4153
# 1 час 9 мин 13 сек
# duration = 400153
# 4 дн 15 час 9 мин 13 сек

# Примечание: можете проверить себя здесь, подумайте, можно ли использовать цикл для проверки
# работы кода сразу для нескольких значений продолжительности, будет ли тут полезен список?

duration = int(input('Введите время в секундах: '))

day = (duration // 86400)
hour = ((duration - (day * 86400)) // 3600)
minute = ((duration - ((day * 86400) + (hour * 3600))) // 60)
seconds = (duration - ((day * 86400) + (hour * 3600) + (minute * 60)))

if duration < 60:
    print(seconds,' сек')
elif duration < 3600:
    print(minute, ' мин', seconds, ' сек')
elif duration < 86400:
    print(hour, ' ч', minute, ' мин', seconds, ' сек')
else:
    print(day, ' дн', hour, ' ч', minute, ' мин', seconds, ' сек')
