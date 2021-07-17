"""
4. Написать программу, которая генерирует в указанных пользователем границах:
случайное целое число;
случайное вещественное число;
случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
"""

from random import randint, uniform


def rand_gen():
    data_type = input('Введите тип данных i(nteger)|f(loat)|c(haracters): ')
    if data_type == 'i':
        start = input('Введите начальное значение: ')
        end = input('Введите конечное значение: ')
        start = int(start)
        end = int(end)
        if start > end:
            start, end = end, start
        r = randint(start, end)
        print(f'Случайное значение в диапазоне от {start} до {end} = {r}')
    elif data_type == 'f':
        start = input('Введите начальное значение: ')
        end = input('Введите конечное значение: ')
        start = float(start)
        end = float(end)
        if start > end:
            start, end = end, start
        r = round(uniform(start, end), 3)
        print(f'Случайное значение в диапазоне от {start} до {end} = {r}')
    elif data_type == 'c':
        start = input('Введите начальное значение: ').lower()
        end = input('Введите конечное значение: ').lower()
        start = ord(start)
        end = ord(end)
        if start > end:
            start, end = end, start
        r = chr(randint(start, end))
        print(f'Случайное значение в диапазоне от {chr(start)} до {chr(end)} = {r}')
    else:
        print(f'Неизвестный тип данных "{data_type}"')


if __name__ == "__main__":
    rand_gen()
