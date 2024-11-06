from math import inf  # Импортируем бесконечность из стандартной библиотеки math

def divide(first, second):
    # Проверяем, является ли второй аргумент нулем
    if second == 0:
        # Если да, возвращаем бесконечность
        return inf
    # Выполняем деление и возвращаем результат
    return first / second