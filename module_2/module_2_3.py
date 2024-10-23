# https://github.com/Garrymag/lessons/blob/master/module_2_3.py

# Исходный список
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

# Индекс для перебора элементов списка
index = 0

# Цикл while для перебора элементов списка
while index < len(my_list):
    # Получаем текущее число
    current_number = my_list[index]

    # Проверяем, является ли число отрицательным
    if current_number < 0:
        break  # Выходим из цикла, если число отрицательное

    # Печатаем положительное число
    print(current_number)

    # Переходим к следующему элементу
    index += 1