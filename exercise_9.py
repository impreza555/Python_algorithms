"""
9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
"""


def medium_num():
    while True:
        first = input('Введите первое число ')
        if first.isdigit():
            break
    while True:
        second = input('Введите второе число ')
        if second.isdigit():
            break
    while True:
        third = input('Введите третье число ')
        if third.isdigit():
            break
    first = int(first)
    second = int(second)
    third = int(third)
    result = ''
    if first > second:
        if second > third:
            result = second
        elif first > third:
            result = third
        else:
            result = first

    elif first < second:
        if first > third:
            result = first
        elif second > third:
            result = third
        else:
            result = second
    return f'Средним числом является {result}'


if __name__ == "__main__":
    print(medium_num())
