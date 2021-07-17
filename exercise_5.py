"""
5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
"""


def positions_alphabet():
    while True:
        letter1 = input('Введите первую букву латинского алфавита ').lower()
        if letter1.isalpha():
            if ord(letter1) not in range(97, 123):
                print('Заданная буква не в диапазоне латинского алфавита')
            else:
                break
        else:
            print('Некорректный ввод')
    while True:
        letter2 = input('Введите вторую букву латинского алфавита ').lower()
        if letter2.isalpha():
            if ord(letter2) not in range(97, 123):
                print('Заданная буква не в диапазоне латинского алфавита')
            else:
                break
        else:
            print('Некорректный ввод')
    res1 = ord(letter1) - 96
    res2 = ord(letter2) - 96
    print(f'Введённые буквы стоят на {res1} и {res2} местах в алфавите\nМежду ними {res2 - res1 - 1} букв')


if __name__ == "__main__":
    positions_alphabet()
