"""
1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""


def multiples():
    mult2 = mult3 = mult4 = mult5 = mult6 = mult7 = mult8 = mult9 = 0
    for el in range(2, 100):
        if not el % 2:
            mult2 += 1
        if not el % 3:
            mult3 += 1
        if not el % 4:
            mult4 += 1
        if not el % 5:
            mult5 += 1
        if not el % 6:
            mult6 += 1
        if not el % 7:
            mult7 += 1
        if not el % 8:
            mult8 += 1
        if not el % 9:
            mult9 += 1
    return f'В диапазоне натуральных чисел от 2 до 99, чисел кратных:\n' \
           f'"2-м" - {mult2}\n"3-м" - {mult3}\n"4-м" - {mult4}\n"5-и" - {mult5}\n' \
           f'"6-и" - {mult6}\n"7-и" - {mult7}\n"8-и" - {mult8}\n"9-и" - {mult9}'


if __name__ == '__main__':
    print(multiples())
