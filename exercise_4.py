"""
4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
"""
el1 = 1  # первый элемент ряда (убывающей геометрической прогрессии)


def sum(n, el1):
    sum0 = 0
    for i in range(n):
        sum0 += el1
        el1 /= -2
    return sum0


# Вариант с рекурсией
def sum_rec(n, el1):
    sum1 = 0
    if n == 1:
        return el1
    sum1 += el1
    el1 /= -2
    return sum1 + sum_rec(n - 1, el1)


if __name__ == '__main__':
    n = int(input('Введите количество "n" суммируемых элементов: '))
    print(f'Сумма {n} элементов ряда = {sum(n, el1)}')
    print(f'Сумма {n} элементов ряда = {sum_rec(n, el1)}')
