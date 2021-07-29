import cProfile
import exercise_4_2 as geometricProgression

"""
1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках
домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
Результаты анализа сохранить в виде комментариев в файле с кодом.
"""

cProfile.run('print(geometricProgression.sum(500, 1))')

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
"""

cProfile.run('print(geometricProgression.sum_rec(500, 1))')

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
"""
