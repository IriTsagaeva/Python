x_chocolate_size = input("Пожалуйста введите количество долек по горизонтали: ")
y_chocolate_size = input("Пожалуйста введите количество долек по вертикали: ")
slice_size = input("Пожалуйста введите какое количество долек нужно отломить: ")
try:
    x_chocolate_size = int(x_chocolate_size)
    y_chocolate_size = int(y_chocolate_size)
    slice_size = int(slice_size)
    if x_chocolate_size <= 0 or y_chocolate_size <= 0 or slice_size <= 0:
        print("Пожалуйста, введите натуральные параметры! Количество долек может быть только натуральным числом!!!")
    elif slice_size % x_chocolate_size == 0 or slice_size % y_chocolate_size == 0:
        print("YES!")
    else:
        print("NO!")
except ValueError:
    print("Пожалуйста, введите параметры в числовом формате!!!")
