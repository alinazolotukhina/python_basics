# Задание 3.
#
# Узнайте у пользователя целое положительное число n.
# Найдите сумму чисел n + nn + nnn.
#
# Пример:
# Введите число n: 3
# n + nn + nnn = 369

input = input('Введите число: ') 

summa = int(input) + int(input+input) + int(input+input+input)
print(f'Сумма равна {summa}') 