# 1. В диапазоне натуральных чисел от 2 до 1000000 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

# keys = [i for i in range(2, 10)]
#
# dict_ = dict.fromkeys(keys, 0)
# print(dict_)
#
# for number in range(2, 1000001):
#     for key in keys:
#         if number % key == 0:
#             dict_[key] += 1
#
# print(dict_)



# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить
# значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля),
# т.к. именно в этих позициях первого массива стоят четные числа.

# import random
#
# random_list = [random.randint(-30, 30) for i in range(10)]
#
# even_index_list = [random_list.index(item) for item in random_list if item % 2 == 0]
#
# print(random_list)
# print(even_index_list)


# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

# import random
#
# random_list = [random.randint(-30, 30) for i in range(10)]
#
# min_index = random_list.index(min(random_list))
# max_index = random_list.index(max(random_list))
#
# print(random_list)
#
# random_list[min_index], random_list[max_index] = random_list[max_index], random_list[min_index]
#
# print(random_list)

# 4. Определить, какое число в массиве встречается чаще всего.

# import random
#
# random_list = [random.randint(0, 10) for i in range(30)]
#
# max_freq = max(zip(list(random_list.count(items) for items in set(random_list)), set(random_list)))
#
# print(random_list)
# print(max_freq)


# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

# import random
#
# random_list = [random.randint(-30, 30) for i in range(10)]
#
# max_below_zero = max([item for item in random_list if item < 0])
#
# print(random_list)
# print(max_below_zero, random_list.index(max_below_zero))

# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

# import random
#
# random_list = [random.randint(-30, 30) for i in range(10)]
#
# min_index = random_list.index(min(random_list))
# max_index = random_list.index(max(random_list))
#
# if min_index < max_index:
#     sum_between_min_and_max = sum([item for item in random_list if min_index < random_list.index(item) < max_index])
# else:
#     sum_between_min_and_max = sum([item for item in random_list if max_index < random_list.index(item) < min_index])
#
# print(random_list)
# print(f'{min_index}, {max_index}')
# print(sum_between_min_and_max)


# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

# import random
#
# random_list = [random.randint(-30, 30) for i in range(10)]
# print(random_list)
#
# first_min = min(random_list)
# random_list.remove(first_min)
# second_min = min(random_list)
#
# print(first_min)
# print(second_min)



# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

# import pprint
#
# matrix = []
#
# for i in range(4):
#     row = []
#     for j in range(5):
#         if j < 4:
#             row.append(int(input(f'Введи число [{i}][{j}]: ')))
#         else:
#             row.append(sum(row))
#     matrix.append(row)
#
# pprint.pprint(matrix)

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

# import random
# import pprint
#
# random_matrix = []
#
# for i in range(6):
#     row = []
#     for j in range(6):
#         row.append(random.randint(-100, 100))
#     random_matrix.append(row)
#
# pprint.pprint(random_matrix)
#
# min_in_columns = [min(column) for column in list(zip(*random_matrix))]
# max_from_min_in_columns = max(min_in_columns)
#
# print()
# print(min_in_columns)
# print(max_from_min_in_columns)

