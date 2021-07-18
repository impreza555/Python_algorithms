"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.
"""


def reverse():
    while True:
        str_num = input('Введите любое число: ')
        if str_num.isdigit():
            break
        else:
            print('Некорректный ввод')
    num = int(str_num[::-1])
    return num


if __name__ == "__main__":
    print(reverse())
