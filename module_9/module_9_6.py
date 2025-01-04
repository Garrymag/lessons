def all_variants(text):
    # Перебираем все возможные длины подпоследовательностей
    for length in range(1, len(text) + 1):
        # Перебираем все возможные начальные позиции подпоследовательностей
        for start in range(len(text) - length + 1):
            # Извлекаем подпоследовательность заданной длины
            subsequence = text[start:start + length]
            # Возвращаем подпоследовательность с помощью yield
            yield subsequence

# Демонстрация работы функции
def main():
    # Создаем генератор для строки "abcd"
    a = all_variants("abcd")

    # Итерируемся по всем подпоследовательностям
    for i in a:
        print(i)

# Запуск основной функции
if __name__ == "__main__":
    main()