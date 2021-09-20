import cProfile
import timeit

"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
Результаты анализа сохранить в виде комментариев в файле с кодом.
"""


# Без использования «Решета Эратосфена»
def search_prime(n):
    count = 1
    number = 1
    prime = [2]

    if n == 1:
        return 2

    while count != n:
        number += 2

        for num in prime:
            if number % num == 0:
                break
        else:
            count += 1
            prime.append(number)

    return number


cProfile.run('search_prime(10)')
print(f"Время выполнения: {timeit.timeit('search_prime(10)', setup='from __main__ import search_prime', number=1000)}")
print()
cProfile.run('search_prime(100)')
print(f"Время выполнения: {timeit.timeit('search_prime(100)', setup='from __main__ import search_prime', number=1000)}")
print()
cProfile.run('search_prime(1000)')
print(
    f"Время выполнения: {timeit.timeit('search_prime(1000)', setup='from __main__ import search_prime', number=1000)}")

"""
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 exercise_2.py:13(search_prime)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        9    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Время выполнения: 0.011702199999999996
"""
"""
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 exercise_2.py:13(search_prime)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
       99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Время выполнения: 0.6552657000000001
"""
"""
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.057    0.057 <string>:1(<module>)
        1    0.057    0.057    0.057    0.057 exercise_2.py:13(search_prime)
        1    0.000    0.000    0.057    0.057 {built-in method builtins.exec}
      999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Время выполнения: 53.67140740000001
"""


# Квадратичная сложность алгоритма: при увеличении количества чисел в 10 раз время выполнения возрастает в 6 раз
# при увеличении количества чисел в 100 раз, время увеличивается в 81 раз


# Используя алгоритм «Решето Эратосфена»
def eratosthenes_sieve(n):
    count = 1
    start = 3
    end = 4 * n

    sieve = [i for i in range(start, end) if i % 2 != 0]
    prime = [2]

    if n == 1:
        return 2

    while count < n:

        for i in range(len(sieve)):

            if sieve[i] != 0:
                count += 1

                if count == n:
                    return sieve[i]

                j = i + sieve[i]

                while j < len(sieve):
                    sieve[j] = 0
                    j += sieve[i]

        prime.extend([i for i in sieve if i != 0])

        start, end = end, end + 2 * n
        sieve = [i for i in range(start, end) if i % 2 != 0]

        for i in range(len(sieve)):

            for num in prime:

                if sieve[i] % num == 0:
                    sieve[i] = 0
                    break


cProfile.run('eratosthenes_sieve(10)')
print(
    f"Время выполнения: {timeit.timeit('eratosthenes_sieve(10)', setup='from __main__ import eratosthenes_sieve', number=1000)}")
print()
cProfile.run('eratosthenes_sieve(100)')
print(
    f"Время выполнения: {timeit.timeit('eratosthenes_sieve(100)', setup='from __main__ import eratosthenes_sieve', number=1000)}")
print()
cProfile.run('eratosthenes_sieve(1000)')
print(
    f"Время выполнения: {timeit.timeit('eratosthenes_sieve(1000)', setup='from __main__ import eratosthenes_sieve', number=1000)}")

"""
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 exercise_2.py:80(eratosthenes_sieve)
        1    0.000    0.000    0.000    0.000 exercise_2.py:85(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       22    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


Время выполнения: 0.012527399999999994
"""
"""
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 exercise_2.py:107(<listcomp>)
        1    0.000    0.000    0.000    0.000 exercise_2.py:110(<listcomp>)
        1    0.000    0.000    0.001    0.001 exercise_2.py:80(eratosthenes_sieve)
        1    0.000    0.000    0.000    0.000 exercise_2.py:85(<listcomp>)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
      345    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}


Время выполнения: 0.6398178
"""
"""
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.047    0.047 <string>:1(<module>)
        2    0.000    0.000    0.000    0.000 exercise_2.py:107(<listcomp>)
        2    0.001    0.000    0.001    0.000 exercise_2.py:110(<listcomp>)
        1    0.045    0.045    0.047    0.047 exercise_2.py:80(eratosthenes_sieve)
        1    0.001    0.001    0.001    0.001 exercise_2.py:85(<listcomp>)
        1    0.000    0.000    0.047    0.047 {built-in method builtins.exec}
     4278    0.001    0.000    0.001    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}


Время выполнения: 44.1234245
"""
# Квадратичная сложность алгоритма: при увеличении количества чисел в 10 раз время выполнения возрастает в 4 раз
# при увеличении количества чисел в 100 раз, время увеличивается в 69 раз

# Вывод: Хотя скорость выполнения двух данных алгоримтов приблизително одинакова, алгоритм «Решето Эратосфена»
# работает немного быстрее.
