# coding: utf-8

# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

number = input("Введи трехзначное число: ")
if len(number) == 3 and number.isdigit():
    sum_ = 0
    mult = 1
    for i in number:
        sum_ += int(i)
        mult *= int(i)

    print(sum_)
    print(mult)
else:
    print("Неверный ввод")


# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
# Объяснить полученный результат.

a = 5  # 0b101
b = 6  # 0b110

print(a & b)   # 0b100 = 4
print(a | b)   # 0b111 = 7
print(a ^ b)   # 0b11 = 3
print(~a)      # 0b1...1111010 = -6
print(a << 2)  # 0b10100 = 20
print(a >> 2)  # 0b1 = 1


# По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b,
# проходящей через эти точки.

try:
    (x1, y1) = map(float, input("Введи координаты первой точки через пробел: ").split())
    (x2, y2) = map(float, input("Введи координаты второй точки через пробел: ").split())

    k = (y1 - y2) / (x1 - x2)
    b = (x2 * y1 - x1 * y2) / (x1 - x2)

    if b >= 0:
        print(
            "Уравнение прямой, проходящей через эти две точки, "
            "имеет вид: y = {}x + {}".format('{0:.2f}'.format(k), '{0:.2f}'.format(abs(b)))
        )
    else:
        print(
            "Уравнение прямой, проходящей через эти две точки, "
            "имеет вид: y = {}x - {}".format('{0:.2f}'.format(k), '{0:.2f}'.format(abs(b)))
        )


except ValueError:
    print("Некорретный ввод")


# Написать программу, которая генерирует в указанных пользователем границах:
#     случайное целое число;
#     случайное вещественное число;
#     случайный символ.

import random
import string

ans = input("Случайное целое (i), вещественное (f) или случайный символ (s): ")

try:
    if ans == 'i':
        min_, max_ = map(int, input("Введи границы через запятую: ").split())
        print(random.randint(min_, max_))

    elif ans == 'f':
        min_, max_ = map(float, input("Введи границы через запятую: ").split())
        print(random.uniform(min_, max_))

    elif ans == 's':
        alph = string.ascii_lowercase
        low_end, high_end = input("Введи границы через запятую (английские строчные буквы): ").split()
        min_index = alph.index(low_end)
        max_index = alph.index(high_end)
        print(random.choice(alph[min_index:max_index]))

    else:
        raise ValueError

except ValueError:
    print("Некорректный ввод")
except IndexError:
    print("Некорректный ввод")


# Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

import string

try:
    alphabet = string.ascii_lowercase
    letter1, letter2 = input("Введи границы через запятую (английские строчные буквы): ").split()

    letter1_index = alphabet.index(letter1)
    letter2_index = alphabet.index(letter2)

    if letter1_index != letter2_index:
        letters_between = abs(letter2_index - letter1_index) - 1
    else:
        letters_between = 0

    print(f'{letter1} стоит на {letter1_index + 1} месте')
    print(f'{letter2} стоит на {letter2_index + 1} месте')
    print(f'Между буквами {letter1} и {letter2} находится {letters_between} букв')

except ValueError:
    print("Некорректный ввод")
except IndexError:
    print("Некорректный ввод")


# Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

import string

alphabet = string.ascii_lowercase

try:
    letter1_index = int(input("Введи номер буквы от 1 до 26: "))
    letter1 = alphabet[letter1_index - 1]

    print(f"На месте {letter1_index} находится буква {letter1}")

except ValueError:
    print("Некорректный ввод")
except IndexError:
    print("Некорректный ввод")


# По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков.
# Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним.

try:
    a, b, c = map(float, input("Введи длины сторон треугольника через запятую (вещественные числа): ").split())

    if a + b > c and a + c > b and b + c > a:
        if a == b and a == c:
            print("Треугольник равносторонний")
        elif a == b or a == c or b == c:
            print("Треугольник равнобедренный")
        else:
            print("Треугольник разносторонний")
    else:
        print("Треугольник несуществует")

except ValueError:
    print("Некорректный ввод")


# Определить, является ли год, который ввел пользователем, високосным или невисокосным.

try:
    year = int(input("Введи год: "))
    if year >= 1582 and year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            print("Год невисокосный")
        else:
            print("Год високосный")
    else:
        print("Год невисокосный")

except ValueError:
    print("Некорректный ввод")


# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

try:
    a, b, c = map(float, input("Введи три вещественных числа: ").split())
    if a == b or a == c or b == c:
        print("Среднего числа среди этих трех нет")
    elif b < a < c or c < a < b:
        print(f"{a} среднее")
    elif a < b < c or a < b < c:
        print(f"{b} среднее")
    else:
        print(f"{c} среднее")

except ValueError:
    print("Некорректный ввод")
