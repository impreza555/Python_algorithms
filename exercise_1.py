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


cProfile.run('print(geometricProgression.sum(10, 1))')
print(
    f"Время выполнения: {timeit.timeit('print(geometricProgression.sum(10, 1))', setup='import exercise_4_2 as geometricProgression', number=100)}")
cProfile.run('print(geometricProgression.sum(100, 1))')
print(
    f"Время выполнения: {timeit.timeit('print(geometricProgression.sum(100, 1))', setup='import exercise_4_2 as geometricProgression', number=100)}")
cProfile.run('print(geometricProgression.sum(990, 1))')
print(
    f"Время выполнения: {timeit.timeit('print(geometricProgression.sum(990, 1))', setup='import exercise_4_2 as geometricProgression', number=100)}")
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

"""
0.666015625
         5 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 exercise_4_2.py:8(sum)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
Время выполнения: 0.0017154000000000058
"""
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
        
Время выполнения: 0.0031104999999999883
"""
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
        
Время выполнения: 0.020294900000000005
"""
# Линейная сложность: При увеличении количества подсчитываемых элементов прогресси в 10 раз время увеличивается в 3 раза
# при увеличении количества элементов в 100 раз время увеличивается в 7 раз


cProfile.run('print(geometricProgression.sum_rec(10, 1))')
print(
    f"Время выполнения: {timeit.timeit('print(geometricProgression.sum_rec(10, 1))', setup='import exercise_4_2 as geometricProgression', number=100)}")
cProfile.run('print(geometricProgression.sum_rec(100, 1))')
print(
    f"Время выполнения: {timeit.timeit('print(geometricProgression.sum_rec(100, 1))', setup='import exercise_4_2 as geometricProgression', number=100)}")
cProfile.run('print(geometricProgression.sum_rec(990, 1))')
print(
    f"Время выполнения: {timeit.timeit('print(geometricProgression.sum_rec(990, 1))', setup='import exercise_4_2 as geometricProgression', number=100)}")
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

"""
0.666015625
         14 function calls (5 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
     10/1    0.000    0.000    0.000    0.000 exercise_4_2.py:17(sum_rec)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       
Время выполнения: 0.002571999999999991
"""
"""
0.6666666666666666
         104 function calls (5 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
    100/1    0.000    0.000    0.000    0.000 exercise_4_2.py:17(sum_rec)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
Время выполнения: 0.007070300000000002
"""
"""
0.6666666666666666
         994 function calls (5 primitive calls) in 0.006 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.006    0.006 <string>:1(<module>)
    990/1    0.006    0.000    0.006    0.006 exercise_4_2.py:17(sum_rec)
        1    0.000    0.000    0.006    0.006 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        
Время выполнения: 0.05928520000000001
"""
# Линейная сложность: При увеличении количества подсчитываемых элементов прогресси в 10 раз время увеличивается в 2.3 раза
# при увеличении количества элементов в 100 раз время увеличивается в 8.4 раз

# Вывод: Хотя разница, в данном примере, незначительна, всё же, первый алгоритм работает быстрее, чем вариант с рекурсией