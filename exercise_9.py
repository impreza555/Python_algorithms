import random

"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""


# random.seed(12)


def max_among_min_in_columns():
    R = 5
    C = 5
    matrix = []
    min_columns_list = []
    for i in range(R):
        matrix.append([random.randint(-50, 50) for i in range(C)])
    for k in range(R):
        tmp = []
        for j in matrix:
            tmp.append(j[k])
        min_columns_list.append(min(tmp))
    print('В матрице:')
    for j in matrix:
        print(j)
    print('-' * 24)
    print(f'Максимальный элемент среди минимальных элементов столбцов матрицы {max(min_columns_list)}')


if __name__ == '__main__':
    max_among_min_in_columns()
