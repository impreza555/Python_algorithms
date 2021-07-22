"""
1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
а должна запрашивать новые данные для вычислений.
Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
"""


def calculator():
    while True:
        try:
            first_num = float(input('Введите первое число '))
            break
        except ValueError:
            print('Вы должны ввести число')
    while True:
        try:
            second_num = float(input('Введите второе число '))
            break
        except ValueError:
            print('Вы должны ввести число')
    while True:
        operator = input('Введите знак операции: "+", "-", "*", "/", либо введите "0" для завершения программы ')
        if operator == '0':
            quit()
        if second_num == 0.0 and operator == "/":
            print('Делить на "0" нельзя... В этом измерении...')
            continue
        if operator == "+" or operator == "-" or operator == "*" or operator == "/":
            break
    if operator == "+":
        result = first_num + second_num
    elif operator == "-":
        result = first_num - second_num
    elif operator == "*":
        result = first_num * second_num
    elif operator == "/":
        result = first_num / second_num
    return f'{first_num} {operator} {second_num} = {result}'


if __name__ == '__main__':
    print(calculator())
