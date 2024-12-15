def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    # Проверяем, является ли numbers итерируемым объектом
    try:
        iter(numbers)
    except TypeError:
        return 0, 0

    # Если numbers - строка, преобразуем в список
    if isinstance(numbers, str):
        numbers = numbers.split(',')

    for item in numbers:
        try:
            # Пытаемся преобразовать элемент в число
            num = float(item)
            result += num
        except (TypeError, ValueError):
            # Увеличиваем счетчик некорректных данных
            incorrect_data += 1
            # Выводим сообщение о некорректных данных
            print(f'Некорректный тип данных для подсчёта суммы - {item}')

    return result, incorrect_data


def calculate_average(numbers):
    # Проверяем тип входных данных
    if not isinstance(numbers, (list, tuple, str)):
        print('В numbers записан некорректный тип данных')
        return None

    try:
        # Вызываем personal_sum для подсчета суммы
        total_sum, _ = personal_sum(numbers)

        # Считаем количество корректных чисел
        count = len([num for num in numbers if isinstance(num, (int, float)) or
                     (isinstance(num, str) and num.replace('.', '').isdigit())])

        # Обрабатываем деление на ноль
        if count == 0:
            return 0

        # Возвращаем среднее арифметическое
        return total_sum / count

    except ZeroDivisionError:
        return 0


# Проверяем работу функций
print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')