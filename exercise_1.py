import cProfile
import timeit
import exercise_4_2 as geometricProgression

"""
1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках
домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
Результаты анализа сохранить в виде комментариев в файле с кодом.
"""


cProfile.run('print(geometricProgression.sum(500, 1))')
print(
    f"Время выполнения: {timeit.timeit('print(geometricProgression.sum(500, 1))', setup='import exercise_4_2 as geometricProgression', number=100)}")
print('*' * 40)
print()

"""
def sum(n, el1):
    sum0 = 0
    for i in range(n):
        sum0 += el1
        el1 *= q
    return sum0
"""
# Линейная сложность: алгоритм проходит один раз от 0 до n прибавляя к сумме следующий элемент

"""
0.6666666666666667
         5 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 exercise_4_2.py:8(sum)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
Время выполнения: 0.011411399999999988
"""

cProfile.run('print(geometricProgression.sum_rec(500, 1))')
print(
    f"Время выполнения: {timeit.timeit('print(geometricProgression.sum_rec(500, 1))', setup='import exercise_4_2 as geometricProgression', number=100)}")
print('*' * 40)

"""
def sum_rec(n, el1):
    sum1 = 0
    if n == 1:
        return el1
    sum1 += el1
    el1 *= q
    return sum1 + sum_rec(n - 1, el1)
"""
# Квадратичная сложность: функция рекурсивно вызывает саму себя, до наступления базового случая.

"""
0.6666666666666666
         504 function calls (5 primitive calls) in 0.002 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.002    0.002 <string>:1(<module>)
    500/1    0.002    0.000    0.002    0.002 exercise_4_2.py:17(sum_rec)
        1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       
Время выполнения: 0.029903999999999986
"""
