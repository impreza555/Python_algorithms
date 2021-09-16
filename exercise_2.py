import random

"""
2. Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить
значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""


def index_even_elements():
    index_list = []
    array = [random.randint(-15, 15) for i in range(15)]
    for idx, el in enumerate(array):
        if el % 2 == 0:
            index_list.append(idx)

    return f'В массиве {array}, чётные элементы находятся под индексами {index_list}'


if __name__ == '__main__':
    print(index_even_elements())
