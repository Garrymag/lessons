def apply_all_func(int_list, *functions):
    # Шаг 1: Создаем пустой словарь для хранения результатов
    results = {}

    # Шаг 2: Перебираем каждую функцию из переданных функций
    for func in functions:
        # Шаг 3: Вызываем функцию с int_list и сохраняем результат
        results[func.__name__] = func(int_list)

    # Шаг 4: Возвращаем словарь результатов
    return results


# Пример функций, которые будут использоваться с apply_all_func
def min_func(int_list):
    return min(int_list)  # Возвращает минимальное значение из списка


def max_func(int_list):
    return max(int_list)  # Возвращает максимальное значение из списка


def len_func(int_list):
    return len(int_list)  # Возвращает количество элементов в списке


def sum_func(int_list):
    return sum(int_list)  # Возвращает сумму всех элементов в списке


def sorted_func(int_list):
    return sorted(int_list)  # Возвращает новый отсортированный список


def average_func(int_list):
    return sum(int_list) / len(int_list) if int_list else 0  # Возвращает среднее значение


# Пример использования
int_list = [12, 4, 75.67, -45, 8.846465849]

# Применяем несколько функций к int_list
result = apply_all_func(int_list, min_func, max_func, len_func, sum_func, sorted_func, average_func)

# Печатаем результаты
print(result)
