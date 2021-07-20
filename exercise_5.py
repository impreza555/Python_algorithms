"""
5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


def ascii():
    i = 0
    for n in range(32, 128):
        i += 1
        if len(str(n)) == 2:
            space = ' '
        else:
            space = ''
        if i == 10:
            end = '\n'
            i = 0
        else:
            end = ''
        print(f'{n}{space} - "{chr(n)}"  |  ', end=end)


if __name__ == "__main__":
    ascii()
