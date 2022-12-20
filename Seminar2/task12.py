# Задача 12
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# Способ 1. С помощью корней квадратного уравнения по теореме Виета

sum = input("Пожалуйста, введите сумму чисел: ")
prod = input("пожалуйста, введите произведение чисел: ")
try:
    sum = int(sum)
    prod = int(prod)
    D = sum**2 - 4 * prod
    if D < 0:
        print("Нет такой пары чисел, которая удовлетворяет заданным параметрам")
    else:
        numberХ = (sum + (D**0.5)) / 2
        numberY = (sum - (D**0.5)) / 2
        if (
            numberХ <= 0
            or numberY <= 0
            or numberХ != int(numberХ)
            or numberY != int(numberY)
            or numberY > 1000
            or numberХ > 1000
        ):
            print(
                f"Нет такой пары натуральных чисел до 1000, которая удовлетворяет заданным параметрам"
            )
        else:
            print(f"Числа загаданные Петей: {int(numberХ)} и {int(numberY)}")
except ValueError:
    print("Пожалуйста, введите параметры в числовом формате!")


# Способ 2. С помошью перебора в циклах

sum = input("Пожалуйста, введите сумму чисел: ")
prod = input("пожалуйста, введите произведение чисел: ")
try:
    sum = int(sum)
    prod = int(prod)
    if sum <= 0 or prod <= 0:
        print(
            f"Нет такой пары натуральных чисел до 1000, которая удовлетворяет заданным параметрам"
        )
    else:
        result = False
        k = 1
        while k <= 10:
            if result == True:
                break
            l = 1
            while l <= 10:
                if l + k == sum and l * k == prod:
                    print(f"Числа загаданные Петей: {k} и {l}")
                    result = True
                    break
                l = l + 1
            k = k + 1
        if result == False:
            print(
                f"Нет такой пары натуральных чисел до 1000, которая удовлетворяет заданным параметрам"
            )
except ValueError:
    print("Пожалуйста, введите параметры в числовом формате!")
