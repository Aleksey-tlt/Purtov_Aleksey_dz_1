# 3.Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов

for i in range(100):
    i = i + 1
    if i:
        print(i, ' процентов')
    elif i % 10 == 1:
        print(i, ' процент')
    elif i % 10 > 1 and i % 10 < 5:
        print(i, ' процента')
    else:
        print(i, ' процентов')
