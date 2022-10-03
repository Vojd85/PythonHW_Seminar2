# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число 
# и показывает сумму его цифр. Через строку нельзя решать.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

def get_int_float_value(inp):
    while True:
        try:
            if '.' in inp:
                value = float(inp)
            elif ',' in inp:
                value = float(inp.replace(',', '.'))
            else: value = int(inp)
        except ValueError:
            inp = input('Это не число! Введите число: ')
        else:
            return value

number = get_int_float_value(input('Введите число: '))

def sum_digit(num):
    sum = 0
    while num % 1 != 0:
        num = round(num*10, 10) # тут не понял почему float нормально не умножается на 10
    num = int(num)
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum

print(sum_digit(number))
