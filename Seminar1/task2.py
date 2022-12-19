# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# Вариант решения 1 для чисел с любым количеством знаков

my_number_str = input("Пожалуйста, введите Ваше число: ")
try:
    my_number = int(my_number_str)
    if my_number < 0:
        my_number = -my_number
    sum = 0
    while my_number > 0:
        sum = sum + my_number % 10
        my_number = my_number // 10
    print(f"Сумма цифр числа равна {sum}")
except ValueError:
    print("Пожалуйста введите данные в числовом формате!!!")

# Вариант решения 2 только для трехзначных чисел

my_number_str = input("Пожалуйста, введите Ваше число: ")
try:
    my_number = int(my_number_str)
    if my_number < 0:
        my_number = -my_number
    if my_number < 1000 and my_number >= 100:
        sum = my_number // 10 // 10 + my_number // 10 % 10 + my_number % 10
        print(f"Сумма цифр числа равна {sum}")
    else:
        print(f"ОШИБКА !!!!\nПожалуйста, введите положительное или отрицательное трехзначное число")
except ValueError:
    print("Пожалуйста введите данные в числовом формате!!!")
