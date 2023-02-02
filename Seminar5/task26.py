def pow(number, power):
    if power == 0:
        return 1
    elif power > 0:
        return number * pow(number, power - 1)
    else:
        return 1 / number * pow(number, power + 1)    
try:
    number = float(input("Введите число: "))
    power = int(input("Введите степень: "))
    print(round(pow(number,power),3))
except ValueError:
    print("Пожалуйста, введите параметры в формате числа!!! Степень обязательно целочисленная!")