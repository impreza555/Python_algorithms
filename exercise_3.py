"""
3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
"""


def equation_straight_line():
    print('Введите координаты точки A(x1;y1):')
    while True:
        x1 = input('\tx1 = ')
        if (x1[0] == '-' and x1[1:].isdigit()) or x1.isdigit():
            break
        else:
            print('Некорректный ввод')
    while True:
        y1 = input('\ty1 = ')
        if (y1[0] == '-' and y1[1:].isdigit()) or y1.isdigit():
            break
        else:
            print('Некорректный ввод')
    x1 = float(x1)
    y1 = float(y1)

    print('Введите координаты точки B(x2;y2):')
    while True:
        x2 = input('\tx2 = ')
        if ((x2[0] == '-' and x2[1:].isdigit()) or x2.isdigit()) and float(x1) != float(x2):
            break
        elif float(x1) == float(x2):
            print('x1 не должен быть равным x2')
        else:
            print('Некорректный ввод')
    while True:
        y2 = input('\ty2 = ')
        if (y2[0] == '-' and y2[1:].isdigit()) or y2.isdigit():
            break
        else:
            print('Некорректный ввод')
    x2 = float(x2)
    y2 = float(y2)

    print('Уравнение прямой, проходящей через эти точки:')
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(' y = %.2f*x + %.2f' % (k, b))


if __name__ == "__main__":
    equation_straight_line()
