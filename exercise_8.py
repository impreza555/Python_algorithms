"""
8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""
R = 4
C = 4


def row(n):
    row = []
    for i in range(n):
        while True:
            el = input(f'Введите элемент строки матрицы ')
            if el.isdigit():
                row.append(int(el))
                break
            else:
                print('Некорректный ввод')
    return row


def matrix(R, C):
    matrix = []
    for i in range(C):
        print(f'Введите строку матрицы\n{"-" * 23}')
        matrix.append(row(R))
    for m_row in matrix:
        m_row.append(sum(m_row))
    print(f'{"-" * 23}')
    for m_row in matrix:
        print(m_row)


if __name__ == '__main__':
    matrix(R, C)
