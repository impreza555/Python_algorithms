import random

"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""


random.seed(12)


def min_it_is_max():
    arr = [random.randint(-100, 100) for i in range(20)]
    print(f'В массиве {arr}, минимальный элемент {min(arr)}, максимальный элемент {max(arr)}')
    arr[arr.index(min(arr))], arr[arr.index(max(arr))] = arr[arr.index(max(arr))], arr[arr.index(min(arr))]
    print(f'Меняем местами {min(arr)} и {max(arr)}, получаем\n{arr}')


if __name__ == '__main__':
    min_it_is_max()
