# Задача 2. Напишите программу, которая принимает на вход число N и 
# выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def get_int_number(num):
    while True:
        try:
            value = int(num)
        except ValueError:
            num = input('Введите натуральное число: ')
        else:
            return value

N = get_int_number(input('Введите число N: '))

def pow_digit(number):
    if number < 0: number = number * -1
    list = []
    key = 1
    for i in range(1, number + 1):
        list.append(i*key)
        key *= i
    print(list)

pow_digit(N)