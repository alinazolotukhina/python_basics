"""
Задание 2. Подсчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной.
При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены, рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены
Используем операции % //. Операции взятия по индексу применять нельзя.
Решите через рекурсию. В задании нельзя применять циклы.
"""


def numbers_sum(num, num_sum):
    
    if num // 10 == 0:
        sum_odd_or_even(num, num_sum)
        
    else:
        sum_odd_or_even(num % 10, num_sum)
        numbers_sum(num // 10, num_sum)

def sum_odd_or_even(num, num_sum):
    
    if num % 2:
        num_sum[1] += num  
    else:
        num_sum[0] += num  

try:  
    number = int(input("Введите целое число: "))
except ValueError:
    print("Введено неверное число")
else:
    sum_of_numbers = [0, 0]
    numbers_sum(number, sum_of_numbers)
    print(
        "сумма четных чисел равна {}, \nсумма нечетных чисел равна {}".format(
            sum_of_numbers[0], sum_of_numbers[1]))
