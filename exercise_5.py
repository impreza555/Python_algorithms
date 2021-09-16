import random

"""
5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""


# random.seed(12)


def max_negative_el():
    arr = [random.randint(-100, 100) for i in range(20)]
    neg_arr = []
    for el in arr:
        if el < 0:
            neg_arr.append(el)
    return f'В массиве {arr} максимальным отрицательным элементом является {max(neg_arr)},' \
           f' на позиции {arr.index(max(neg_arr)) + 1}'


if __name__ == '__main__':
    print(max_negative_el())
