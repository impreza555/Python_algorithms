import collections

"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
чья прибыль выше среднего и отдельно вывести наименования предприятий,
чья прибыль ниже среднего.
Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections
"""

Company = collections.namedtuple('Company', ['name', 'q1', 'q2', 'q3', 'q4', 'year'])


def data_input(i):
    name = input(f'Введите имя {i} компании: ')
    while True:
        q1 = input('Введите прибыль 1 кв: ')
        if q1.isdigit():
            q1 = float(q1)
            break
        else:
            print('Некорректный ввод')
    while True:
        q2 = input('Введите прибыль 2 кв: ')
        if q2.isdigit():
            q2 = float(q2)
            break
        else:
            print('Некорректный ввод')
    while True:
        q3 = input('Введите прибыль 3 кв: ')
        if q3.isdigit():
            q3 = float(q3)
            break
        else:
            print('Некорректный ввод')
    while True:
        q4 = input('Введите прибыль 3 кв: ')
        if q4.isdigit():
            q4 = float(q4)
            break
        else:
            print('Некорректный ввод')
    year = round(q1 + q2 + q3 + q4, 2)
    return name, q1, q2, q3, q4, year


def calculation_profit(x):
    average_profit = 0
    winners = []
    losers = []
    for _ in range(x):
        average_profit += companies[_].year
    average_profit = round(average_profit / n, 2)
    for _ in range(x):
        if companies[_].year > average_profit:
            winners.append(companies[_])
        else:
            losers.append(companies[_])
    return average_profit, winners, losers


if __name__ == '__main__':
    while True:
        n = input('Введите количество предприятий: ')
        if n.isdigit():
            n = int(n)
            break
        else:
            print('Некорректный ввод')
    companies = [Company(*data_input(i + 1)) for i in range(n)]
    print('_' * 60)
    if n == 1:
        print('Для расчёта представлены данные одного предприятия: {} его годовая прибыль: {}'
              ' '.format(companies[0].name, companies[0].year))
    else:
        comp = calculation_profit(n)
        print('Cредняя прибыль за год для всех предприятий: {0}{1}{2}'.format(comp[0], '\n', '_' * 60))
        print(f'Предприятия с прибылью больше годовой:\n{"_" * 60}')
        for _ in comp[1]:
            print(f'{_.name}, годовая прибыль {_.year}')
        print('_' * 60)
        print(f'Предприятия с прибылью меньше годовой:\n{"_" * 60}')
        for _ in comp[2]:
            print(f'{_.name}, годовая прибыль {_.year}')
