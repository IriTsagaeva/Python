# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def summ(first_summand, second_summand):
    if first_summand>=0 and second_summand>=0:
        if second_summand == 0:
            return first_summand
        else:
            return first_summand + sum(1, second_summand - 1)
    else:
        print("Числа должны быть неотрицательными!!!")


try:
    number = int(input("Введите число 1: "))
    power = int(input("Введите число 2: "))
    result = summ(number,power)
    if result != None:
        print(f"Sum = {result}")
except ValueError:
    print("Пожалуйста, введите параметры в формате числа!!! Числа обязательно целые!")