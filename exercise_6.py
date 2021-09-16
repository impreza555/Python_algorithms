import random

"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
# random.seed(12)


def amount_between_max_min():
    arr = [random.randint(-50, 50) for i in range(20)]
    min_id = 0
    max_id = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min_id]:
            min_id = i
        elif arr[i] > arr[max_id]:
            max_id = i
    if min_id > max_id:
        min_id, max_id = max_id, min_id
    sum = 0
    for i in range(min_id + 1, max_id):
        sum += arr[i]
    return f'В массиве {arr}\nМинимальный элемент {arr[min_id]}\nМаксимальный элемент {arr[max_id]}' \
           f'\nСумма элементов между ними {sum}'


if __name__ == '__main__':
    print(amount_between_max_min())
