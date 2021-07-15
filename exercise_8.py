"""
8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
"""


def leap_year():
    while True:
        year = input('Введите желаемый год ')
        if len(year) == 4 and year.isdigit():
            break
        else:
            print('Некорректный ввод')
    year = int(year)
    yes = f'{year} год является високосным'
    no = f'{year} год не является високосным'
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return yes
            else:
                return no
        return yes
    else:
        return no


if __name__ == "__main__":
    print(leap_year())
