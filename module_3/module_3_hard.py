def calculate_structure_sum(*args):
    # Инициализируем переменную для хранения общей суммы
    total = 0

    def recursive_sum(item):
        nonlocal total  # Указываем, что будем использовать переменную total из внешней области видимости

        # Проверяем, является ли элемент числом
        if isinstance(item, (int, float)):
            total += item  # Добавляем число к общей сумме
        # Проверяем, является ли элемент строкой
        elif isinstance(item, str):
            total += len(item)  # Добавляем длину строки к общей сумме
        # Проверяем, является ли элемент списком, кортежем или множеством
        elif isinstance(item, (list, tuple, set)):
            for element in item:
                recursive_sum(element)  # Рекурсивно вызываем для каждого элемента
        # Проверяем, является ли элемент словарем
        elif isinstance(item, dict):
            for key, value in item.items():
                recursive_sum(key)  # Рекурсивно вызываем для ключа
                recursive_sum(value)  # Рекурсивно вызываем для значения

    # Обрабатываем каждый аргумент, переданный в функцию
    for arg in args:
        recursive_sum(arg)  # Вызываем рекурсивную функцию для текущего аргумента

    return total  # Возвращаем общую сумму


# Пробуем использовать
data_structure = [
    [1, 2, 3],  # Список с числами
    {'a': 4, 'b': 5},  # Словарь с числовыми значениями
    (6, {'cube': 7, 'drum': 8}),  # Кортеж с числом и словарем
    "Hello",  # Строка
    ((), [{(2, 'Urban', ('Urban2', 35))}])  # Вложенные структуры
]

# Вызываем функцию и сохраняем результат
result = calculate_structure_sum(data_structure)
print(result)