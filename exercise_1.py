import hashlib

"""
1. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""


def substring_count(input_string):
    hash_set = set()
    for i in range(len(input_string) + 1):
        for j in range(i + 1, len(input_string) + 1):
            h = hashlib.sha1(input_string[i:j].encode('utf-8')).hexdigest()
            hash_set.add(h)
    return len(hash_set)


if __name__ == '__main__':
    some_string = input('Введите строку ').lower()
    print(f'Количество различных подстрок в строке {some_string}: {substring_count(some_string)}')
