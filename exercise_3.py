import random

"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""


# random.seed(12)


def min_it_is_max():
    arr = [random.randint(-100, 100) for i in range(15)]
    min_el = min(arr)
    max_el = max(arr)
    print(f'В массиве {arr}, минимальный элемент {min_el}, максимальный элемент {max_el}')
    arr[arr.index(min_el)] = max_el
    arr[arr.index(max_el)] = min_el
    # arr[arr.index(min(arr))], arr[arr.index(max(arr))] = arr[arr.index(max(arr))], arr[arr.index(min(arr))]
    print(f'Меняем местами {min_el} и {max_el}, получаем\n{arr}')


if __name__ == '__main__':
    min_it_is_max()
