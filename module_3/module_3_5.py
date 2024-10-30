def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Если длина строки больше 1
    if len(str_number) > 1:
        # Берем первую цифру
        first = int(str_number[0])
        # Рекурсивно умножаем на результат функции с оставшимися цифрами
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        # Если осталась только одна цифра, возвращаем её как результат
        return int(str_number)


# Пример использования функции
result = get_multiplied_digits(402035)

# Вывод результата на консоль
print(result)