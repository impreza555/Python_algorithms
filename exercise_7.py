import random

"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""


# random.seed(12)


def two_min_el():
    arr = [random.randint(-50, 50) for i in range(20)]
    arr_copy = arr.copy()
    min1 = min(arr_copy)
    arr_copy.remove(min1)
    min2 = min(arr_copy)
    return f'В массиве {arr}\nпервый наименьший элемент {min1}\nвторой наименьший элемент {min2}'


if __name__ == '__main__':
    print(two_min_el())
