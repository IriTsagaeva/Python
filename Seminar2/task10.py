# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2

# Считается, что орел - это 1, а решка - это 0

from random import randint

n = input("Пожалуйста, введите количество монеток: ")
try:
    n = int(n)
    if n <= 1:
        print("Пожалуйста, введите положительное количество монеток больше 1")
    else:
        k = 0
        heads_count = 0
        while k < n:
            head_or_tail = randint(0, 1)
            print(f"{head_or_tail}", end=" ")
            heads_count = heads_count + head_or_tail
            k = k + 1
        print()
        tails_count = n - heads_count
        if heads_count >= tails_count:
            # Здесь в зависимости от числа определяем падеж слова "монетка"
            if tails_count % 100 >= 11 and tails_count % 100 <= 14:
                word = "монеток"
            elif tails_count % 10 == 1:
                word = "монетку"
            elif tails_count % 10 >= 2 and tails_count % 10<= 4:
                word = "монетки"
            else:
                word = "монеток"
            print(f"Нужно перевернуть {tails_count} {word}")
        else:
            # Здесь в зависимости от числа определяем падеж слова "монетка"
            if heads_count % 100 >= 11 and heads_count % 100 <= 14:
                word = "монеток"
            elif heads_count % 10 == 1:
                word = "монетку"
            elif heads_count % 10 >= 2 and heads_count % 10 <= 4:
                word = "монетки"
            else:
                word = "монеток"
            print(f"Нужно перевернуть {heads_count} {word}")
except ValueError:
    print("ОШИБКА!!! Пожалуйста, введите параметр в числовом формате!")
