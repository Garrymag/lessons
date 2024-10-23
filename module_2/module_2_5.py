# https://github.com/Garrymag/lessons/blob/master/module_2/module_2_5.py


# Объявляем функцию
def get_matrix(n, m, value):
    # Создаем пустой список для матрицы
    matrix = []

    # Внешний цикл для строк
    for i in range(n):
        # Создаем пустой список для строки
        row = []

        # Внутренний цикл для столбцов
        for j in range(m):
            # Добавляем значение в строку
            row.append(value)

        # Добавляем заполненную строку в матрицу
        matrix.append(row)

    # Возвращаем заполненную матрицу
    return matrix


# Проба использования функции
result = get_matrix(3, 4, 7)
print(result)