# HW04

# 1. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.

# from math import sqrt
# import memory_profiler


# @memory_profiler.profile
# def straight_search(numbers_of_primes):
#     list_of_primes = []
#     current_number = 2
#
#     while len(list_of_primes) < numbers_of_primes:
#         is_prime = True
#         for i in range(2, current_number // 2 + 1):
#             if current_number % i == 0:
#                 is_prime = False
#                 break
#
#         if is_prime is True:
#             list_of_primes.append(current_number)
#
#         current_number += 1
#
#     print(list_of_primes)
#     print(f'{numbers_of_primes} по счету простое число - это {list_of_primes[-1]}')

# Формально, это не совсем решето Эратосфена, так как само решето позволяет найти все простые числа в диапазоне.
# В задаче диапазон заранее неизвестен, будем добавлять в лист простые числа и каждое следующее число проверять,
# не делится ли оно на одно из уже существующих делителей

# @memory_profiler.profile
# def sieve_of_eratosthenes(numbers_of_primes):
#     list_of_primes = []
#     current_number = 2
#
#     while len(list_of_primes) < numbers_of_primes:
#         is_prime = True
#         for item in list_of_primes:
#
#             if item > sqrt(current_number) + 1:
#                 break
#
#             if current_number % item == 0:
#                 is_prime = False
#                 break
#
#         if is_prime is True:
#             list_of_primes.append(current_number)
#
#         current_number += 1
#
#     print(list_of_primes)
#     print(f'{numbers_of_primes} по счету простое число - это {list_of_primes[-1]}')
#
#
# # straight_search(10)
# sieve_of_eratosthenes(10)


# 2. Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.


# import timeit
# import statistics
#
# statement = "straight_search(1000)"
# setup = "from __main__ import straight_search"
# statement2 = "sieve_of_eratosthenes(1000)"
# setup2 = "from __main__ import sieve_of_eratosthenes"
#
# print(statistics.mean(timeit.repeat(statement, setup=setup, repeat=100, number=1)))
# print(statistics.mean(timeit.repeat(statement2, setup=setup2, repeat=100, number=1)))

# Среднее время выполнения первой реализации (прямого находления с перебором всех возможных делителей) 0.364 сек
# Вторая реализация с использованием решета Эратосфена и перебором делителей до корня текущего числа работает за 0.029
# Итого при нахождении 1000 простых чисел, второй алгоритм работает в 12 раз быстрее. На больших числах это значение
# будет расти






# HW06

# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах
# в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Анализ проводил на задачах поиска простых чисел, описанных выше. По данным memory_profiler обе реализации
# используют одинаковое количество памяти (34.9 MiB). Однако мне не удалось получить построчные
# комментарии (как и на уроке)
# Можно сделать вывод, что узкое место в алгоритмах это все-таки непосредственно логика решения задачи.
# Система Windows 7, 64bit





# HW05

# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

# import collections
# import statistics
#
# FactoryRecord = collections.namedtuple('FactoryRecord', 'name, average_income')
# Database = []
#
# FactoryCounter = int(input("Количество компаний: "))
#
# for i in range(FactoryCounter):
#     UserInput = str(input('Введи имя и прибыль через запятую: ')).split(sep=', ')
#
#     for item in UserInput:
#         UserInput[UserInput.index(item)] = float(item) if item.isdigit() else item
#
#     average_income = statistics.mean(UserInput[1:])
#
#     NewRecord = FactoryRecord(UserInput[0], average_income)
#     Database.append(NewRecord)
#
#
# average_income_total = statistics.mean([item.average_income for item in Database])
# less_than_mean = [item.name for item in Database if item.average_income <= average_income_total]
# more_than_mean = [item.name for item in Database if item.average_income > average_income_total]
#
# print(f'Прибыль больше среднего у компаний {more_than_mean}, меньше у {less_than_mean}')


# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


# import collections
#
#
# def hex_to_dec(hex_number):
#
#     hex_table = {
#         '0': 0,
#         '1': 1,
#         '2': 2,
#         '3': 3,
#         '4': 4,
#         '5': 5,
#         '6': 6,
#         '7': 7,
#         '8': 8,
#         '9': 9,
#         'A': 10,
#         'B': 11,
#         'C': 12,
#         'D': 13,
#         'E': 14,
#         'F': 15
#     }
#
#     decimal_number = 0
#     for item in hex_number:
#         decimal_number += hex_table.get(item) * 16 ** (len(hex_number) - hex_number.index(item) - 1)
#     return decimal_number
#
#
# def dec_to_hex(dec_number):
#
#     hex_table = {
#         0: '0',
#         1: '1',
#         2: '2',
#         3: '3',
#         4: '4',
#         5: '5',
#         6: '6',
#         7: '7',
#         8: '8',
#         9: '9',
#         10: 'A',
#         11: 'B',
#         12: 'C',
#         13: 'D',
#         14: 'E',
#         15: 'F'
#     }
#
#     hex_number = collections.deque()
#     while dec_number >= 16:
#         hex_number.appendleft(hex_table.get(dec_number % 16))
#         dec_number = dec_number // 16
#     hex_number.appendleft(hex_table.get(dec_number % 16))
#
#     return list(hex_number)
#
#
# a = list(input("Введи первое 16-ричное число: "))
# b = list(input("Введи второе 16-ричное число: "))
#
# sum_ = dec_to_hex(hex_to_dec(a) + hex_to_dec(b))
# mult_ = dec_to_hex(hex_to_dec(a) * hex_to_dec(b))
#
# print(f'{a} + {b} = {sum_}')
# print(f'{a} * {b} = {mult_}')







#HW07

# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).


# import random
#
#
# def bubble_sort(list_to_sort):
#     for i in range(0, len(list_to_sort) - 1):
#         is_sorted = True
#         for j in range(0, len(list_to_sort) - i - 1):
#             if list_to_sort[j] > list_to_sort[j+1]:
#                 list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]
#                 is_sorted = False
#         if is_sorted:
#             break
#     return list_to_sort
#
#
# list_to_sort = [random.randint(-100, 100) for _ in range(30)]
# print(list_to_sort)
# print(bubble_sort(list_to_sort))


# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
#
#
# import random
#
#
# def merge_sort(list_to_sort):
#     if len(list_to_sort) > 1:
#         list1 = merge_sort(list_to_sort[: len(list_to_sort) // 2])
#         list2 = merge_sort(list_to_sort[len(list_to_sort) // 2:])
#         result = merge(list1, list2)
#         return result
#     else:
#         return list_to_sort
#
#
# def merge(sorted_list1, sorted_list2):
#     merged_list = []
#     while len(sorted_list1) > 0 and len(sorted_list2) > 0:
#         if sorted_list1[0] <= sorted_list2[0]:
#             to_add = sorted_list1.pop(0)
#             merged_list.append(to_add)
#         else:
#             to_add = sorted_list2.pop(0)
#             merged_list.append(to_add)
#     if len(sorted_list1) != 0:
#         merged_list.extend(sorted_list1)
#     else:
#         merged_list.extend(sorted_list2)
#
#     return merged_list
#
#
# list_to_sort = [float('{:.2f}'.format(random.random() * 50)) for _ in range(30)]
#
# print(list_to_sort)
# print(merge_sort(list_to_sort))

# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# то используйте метод сортировки, который не рассматривался на уроках

# import random
#
#
# def median_search(list_to_search, target):
#     while True:
#         if len(list_to_search) <= 2:
#             if target == 0:
#                 return list_to_search[0]
#             else:
#                 return list_to_search[1]
#
#         pivot = random.randint(0, len(list_to_search) - 1)
#
#         list1 = [item for item in list_to_search if item <= list_to_search[pivot]]
#         list2 = [item for item in list_to_search if item > list_to_search[pivot]]
#
#         if len(list1) - 1 == target:
#             return list_to_search[pivot]
#         elif len(list1) - 1 < target:
#             target -= len(list1)
#             list_to_search = list2
#         else:
#             list_to_search = list1
#
# m = 10
#
# list_to_search = [random.randint(-50, 50) for _ in range(2 * m + 1)]
#
# print(sorted(list_to_search))
# print(median_search(list_to_search, m))




