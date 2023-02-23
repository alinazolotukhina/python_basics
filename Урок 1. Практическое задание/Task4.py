# Задание 4.
#
# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите
# прибыль фирмы в расчете на одного сотрудника.
#
# Пример:
# Введите выручку фирмы: 1000
# Введите издержки фирмы: 500
# Финансовый результат - прибыль. Ее величина: 500
# Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
# Рентабельность выручки = 0.5
# Введите численность сотрудников фирмы: 10
# Прибыль фирмы в расчете на одного сотрудника = 50.0

earnings = int(input('Введите доход фирмы: '))  # выручка
costs = int(input('Введите расход фирмы: '))  # издержки

if earnings > costs:  # прибыль
    profit = earnings - costs  # находим прибыль
    print("Финансовый результат - прибыль. Ее величина: {}".format(profit))
    # находим рентабельность
    print("Рентабельность выручки = {}".format(round(costs / earnings, 2)))
    # вводим количество сотрудников и находим прибыль на одного сотрудника
    employees = int(input('Введите количество сотрудников: '))
    print('Прибыль фирмы в расчете на одного сотрудника = {}'.format(
        round(profit / employees, 2)))
elif earnings < costs:  # убыль
    print("Финансовый результат - убыток. Его величина: {}".format(
        costs - earnings))
else: 
    print("Доход и расход равны")