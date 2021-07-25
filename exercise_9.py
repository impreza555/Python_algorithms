import random

"""
9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""


def max_among_min_in_columns():
    matrix = []
    min_columns_list = []
    for i in range(5):
        matrix.append([random.randint(-50, 50) for i in range(5)])


    print(matrix)

max_among_min_in_columns()