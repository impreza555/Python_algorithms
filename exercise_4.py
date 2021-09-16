import random

"""
4. Определить, какое число в массиве встречается чаще всего.
"""


# random.seed(12)


def max_count():
    arr = [random.randint(0, 10) for i in range(20)]
    max_cnt = 1
    elem = arr[0]
    print(f'Имеем массив {arr}')
    for el in arr:
        cnt_el = arr.count(el)
        if cnt_el > max_cnt:
            max_cnt = cnt_el
            elem = el
    return f'Число {elem} повторяется {max_cnt} раз'


if __name__ == '__main__':
    print(max_count())
