import random

"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""


# По убыванию:
def bubble_sort(arr):
    for j in range(len(arr) - 1):
        for i in range(len(arr) - 1 - j):
            if arr[len(arr) - 1 - i] > arr[len(arr) - 2 - i]:
                arr[len(arr) - 1 - i], arr[len(arr) - 2 - i] = arr[len(arr) - 2 - i], arr[len(arr) - 1 - i]
    return arr


# По возрастанию:
# def bubble_sort(arr):
#     for j in range(len(arr) - 1):
#         for i in range(len(arr) - 1 - j):
#             if arr[len(arr) - 1 - i] < arr[len(arr) - 2 - i]:
#                 arr[len(arr) - 1 - i], arr[len(arr) - 2 - i] = arr[len(arr) - 2 - i], arr[len(arr) - 1 - i]
#     return arr

if __name__ == '__main__':
    a = [random.randint(-100, 100) for i in range(20)]
    # a = [64, -10, -61, 92, 72, -47, -81, -75, -99, -8]
    print(f'Исходный массив:\n{a}')
    print(f'Отсортированный массив:\n{bubble_sort(a)}')
