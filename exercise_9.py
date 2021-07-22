"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""


def largest_sum_digits():
    user_input = input('Введите через пробел несколько чисел ').split()
    max_sum = 0
    sum_d = 0
    for el in user_input:
        for d in el:
            sum_d += int(d)
        if sum_d > max_sum:
            max_sum = sum_d
            max_num = el
        sum_d = 0
    return f'Наибольшим по сумме цифр числом, среди введённых чисел {", ".join(user_input)},' \
           f' является число {max_num}, сумма цифр равна {max_sum}'


if __name__ == '__main__':
    print(largest_sum_digits())
