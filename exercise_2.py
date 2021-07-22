"""
2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""


def count_even_odd():
    even = 0
    odd = 0
    even_list = []
    odd_list = []
    while True:
        str_num = input('Введите любое число: ')
        if str_num.isdigit():
            break
        else:
            print('Некорректный ввод')
    for n in str_num:
        if int(n) % 2 == 0:
            even += 1
            even_list.append(n)
        else:
            odd += 1
            odd_list.append(n)
    print(
        f'В введённом числе {even} чётных цифр(ы): ({", ".join(even_list)}), и {odd} нечётных ({", ".join(odd_list)})')


if __name__ == "__main__":
    count_even_odd()
