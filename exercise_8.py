"""
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""


def counting_occurrences():
    sequence = input('Введите через пробел последовательность чисел ').split()
    num = input('Введите цифру ')
    count = 0
    for el in sequence:
        for d in el:
            if d == num:
                count += 1
    return f'В последовательности {sequence} цифра {num} встречается {count} раз(а)'


if __name__ == "__main__":
    print(counting_occurrences())
