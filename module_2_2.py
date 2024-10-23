# https://github.com/Garrymag/lessons/blob/master/module_2_2.py

# Ввод трех целых чисел
first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))

# Условная конструкция для проверки равенства1
if first == second == third:
    print(3)  # Все числа равны
elif first == second or first == third or second == third:
    print(2)  # Два числа равны
else:
    print(0)  # Все числа разные