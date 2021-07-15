"""
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""


def sum_mult():
    while True:
        my_var = input('Введите трёхзначное число ')
        if len(my_var) == 3 and my_var.isdigit():
            break
        else:
            print('Некорректный ввод')
    a, b, c = int(my_var[0]), int(my_var[1]), int(my_var[2])
    my_sum = a + b + c
    my_mult = a * b * c
    print(f'Сумма цифр введённого числа равна: {my_sum}')
    print(f'Произведение цифр введённого числа равно: {my_mult}')


if __name__ == "__main__":
    sum_mult()
