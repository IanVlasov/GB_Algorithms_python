# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться,
# а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
# то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.


def addition():
    try:
        a = float(input("Введи первое слагаемое: "))
        b = float(input("Введи второе слагаемое: "))
        print(f"{a} + {b} = {a + b}\n")

    except ValueError:
        print("Некорректный ввод! Попробуй еще раз")
        addition()


def subtraction():
    try:
        a = float(input("Введи уменьшаемое: "))
        b = float(input("Введи вычитаемое: "))
        print(f"{a} - {b} = {a - b}\n")

    except ValueError:
        print("Некорректный ввод! Попробуй еще раз")
        subtraction()


def multiplication():
    try:
        a = float(input("Введи первый множитель: "))
        b = float(input("Введи второй множитель: "))
        print(f"{a} * {b} = {a * b}\n")

    except ValueError:
        print("Некорректный ввод! Попробуй еще раз")
        multiplication()


def division():
    try:
        a = float(input("Введи делимое: "))
        b = float(input("Введи делитель: "))
        if b == 0:
            print("На ноль делить нельзя!\n")
        else:
            print(f"{a} / {b} = {a / b}\n")

    except ValueError:
        print("Некорректный ввод! Попробуй еще раз")
        division()


operations = {
    "0": exit,
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}

while True:
    user_choice = input("Выбери действие (+, -, *, / или 0(ноль) для выхода: ")

    if operations.get(user_choice) is None:
        print("Некорректный ввод")
        continue
    else:
        operations.get(user_choice)()


# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

while True:
    try:
        number = input("Введи натуральное число: ")

        if int(number) > 0:
            counter_even = 0
            even = []
            counter_odd = 0
            odd = []

            for digit in number:
                if int(digit) % 2 == 0:
                    counter_even += 1
                    even.append(digit)
                else:
                    counter_odd += 1
                    odd.append(digit)

            print(f"В числе {number} {counter_even} четные цифры {even} и {counter_odd} нечетные {odd}")

            break

        else:
            raise ValueError

    except ValueError:
        print("Некорректный ввод")


# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

while True:
    try:
        number = input("Введи натуральное число: ")

        if int(number) > 0:
            print(number[::-1])

        else:
            raise ValueError

    except ValueError:
        print("Некорректный ввод")


# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

while True:
    try:
        n = int(input("Введи количество элементов последовательности (больше 0): "))

        if int(n) > 0:
            control_list = [1]

            for i in range(1, n):
                next_element = 1 / 2 ** i

                if i % 2 == 0:
                    control_list.append(next_element)

                else:
                    control_list.append(-next_element)

            sum_ = sum(control_list)

            print(control_list)
            print(f'сумма {n} элементов равна {sum_}')

        else:
            raise ValueError

    except ValueError:
        print("Некорректный ввод")


# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

for i in range(32, 128):
    if (i - 1) % 10 != 0:
        if i < 100:
            print(f'{i} : {chr(i)}', end=' | ')
        else:
            print(f'{i}: {chr(i)}', end=' | ')
    else:
        print(f'{i}: {chr(i)}')


# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

import random

hidden_number = random.randint(0, 100)
attempt_counter = 10
print("Какое число от 0 до 100 я загадал?")

while True:

    try:
        while attempt_counter != 0:
            print(f'Осталось {attempt_counter} попыток')
            players_number = int(input("Твоя версия: "))

            if 0 <= players_number <= 100:

                if players_number == hidden_number:
                    print(f'\nПоздравляю! Ты угадал число {hidden_number} с {attempt_counter} попыток!')
                    break

                elif players_number > hidden_number:
                    print('Неверно! Мое число меньше!')
                    attempt_counter -= 1

                else:
                    print('Неверно! Мое число больше!')
                    attempt_counter -= 1

            else:
                raise ValueError

        print(f'Ты проиграл! Это было число {hidden_number}')
        break

    except ValueError:
        print("Некорректный ввод")


# 7. Напишите программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
# где n - любое натуральное число.

while True:
    try:
        n = int(input("Введи натуральное число: "))

        if n > 0:
            left_part = sum(range(1, n+1))
            right_part = n * (n + 1)/2

            print(f'1+2+...+n = {left_part} (n = {n})')
            print(f'n(n+1)/2 = {right_part} (n = {n})')

            if left_part == right_part:
                print("Все верно!")
            else:
                print("Что-то пошло не так")

            break

        else:
            raise ValueError

    except ValueError:
        print("Некорректный ввод")


# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

while True:
    try:
        number_to_check = input("Введи число, по которому будет произведен поиск: ")

        if number_to_check.isdigit():
            number_to_search = input("Введи цифру, которую необходимо найти (от 0 до 9): ")

            if 0 <= int(number_to_search) <= 9:
                counter = 0

                for digit in number_to_check:
                    if digit == number_to_search:
                        counter += 1

                print(f'В числе {number_to_check} цифра {number_to_search} встречается {counter} раз')
                break

            else:
                raise ValueError
        else:
            raise ValueError

    except ValueError:
        print("Некорректный ввод")


# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

while True:
    try:
        string_of_numbers = input(f'Введи числа для проверки через пробел: ').split(' ')

        for number in string_of_numbers:
            if int(number) < 0:
                raise ValueError

        sum_of_searched_number = 0
        searched_number = []

        for number in string_of_numbers:
            current_sum = 0

            for digit in number:
                current_sum += int(digit)

            if current_sum > sum_of_searched_number:
                searched_number.clear()
                searched_number.append(number)
                sum_of_searched_number = current_sum

            elif current_sum == sum_of_searched_number:
                searched_number.append(number)

        output_string = ', '.join(searched_number)

        print(f'Наибольшее число из введенных по сумме цифр - это {output_string}\n'
              f'Сумма цифр равна {sum_of_searched_number}')

        break

    except ValueError:
        print("Некорректный ввод")
