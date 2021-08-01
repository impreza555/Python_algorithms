import collections

"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections
"""


def addition_hex_numbers(a, b):
    hex_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
               '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
               'F': 15}
    num_hex = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
               5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E',
               15: 'F'}
    a = collections.deque(a)
    b = collections.deque(b)
    result = collections.deque()
    if len(a) > len(b):
        while len(a) != len(b):
            b.appendleft('0')
    else:
        while len(a) != len(b):
            a.appendleft('0')
    digit = 0
    while a:
        res = hex_num.get(a.pop()) + hex_num.get(b.pop()) + digit
        if res < 16:
            result.appendleft(num_hex.get(res))
            digit = 0
        else:
            res -= 16
            result.appendleft(num_hex.get(res))
            digit = 1
    if digit:
        result.appendleft(digit)
    return list(result)


def multiplication_hex_numbers():
    pass


A = list(input('Введите 1-е шестнадцатиричное число: ').upper())
B = list(input('Введите 2-е шестнадцатиричное число: ').upper())
print(*A, '+', *B, '=', *addition_hex_numbers(A, B))
