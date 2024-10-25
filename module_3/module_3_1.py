# Глобальная переменная для подсчета вызовов функций
calls = 0


def count_calls():
    # Объявляем, что будем использовать глобальную переменную 'calls'
    global calls
    # Увеличиваем значение переменной 'calls' на 1 каждый раз, когда вызывается эта функция
    calls += 1


def string_info(string):
    # Вызываем функцию count_calls, чтобы увеличить счетчик вызовов
    count_calls()

    # Возвращаем кортеж, содержащий:
    # 1. Длину строки
    # 2. Строку в верхнем регистре
    # 3. Строку в нижнем регистре
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):
    # Вызываем функцию count_calls, чтобы увеличить счетчик вызовов
    count_calls()
    list_to_search_low = []
    # Запишем список для поиска в новый список в нижнем регистре
    for item in list_to_search:
        list_to_search_low.append(item.lower())
    # Приводим искомую строку к нижнему регистру для сравнения
    string_lower = string.lower()

    # Проверяем, содержится ли искомая строка в списке (также приведенном к нижнему регистру)

    return string_lower in list_to_search_low


# Примеры вызовов функций
# Вызываем string_info с аргументом 'Capybara' и печатаем результат
print(string_info('Capybara'))  # Ожидаем (8, 'CAPYBARA', 'capybara')

# Вызываем string_info с аргументом 'Armageddon' и печатаем результат
print(string_info('Armageddon'))  # Ожидаем (10, 'ARMAGEDDON', 'armageddon')

# Проверяем, содержится ли строка 'Urban' в списке ['ban', 'BaNaN', 'urBAN'] (регистронезависимо)
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Ожидаем True

# Проверяем, содержится ли строка 'cycle' в списке ['recycling', 'cyclic']
print(is_contains('cycle', ['recycling', 'cyclic']))  # Ожидаем False

# Выводим количество вызовов всех функций
print(calls)  # Ожидаем 4, так как было 2 вызова string_info и 2 вызова is_contains