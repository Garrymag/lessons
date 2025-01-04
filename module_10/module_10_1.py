# Импортируем необходимые модули
from time import sleep  # Для создания паузы между операциями
import threading  # Для работы с потоками
import time  # Для измерения времени выполнения


def write_words(word_count, file_name):
    """
    Функция для записи слов в файл с паузой между записями

    :param word_count: Количество слов для записи
    :param file_name: Имя файла для записи
    """
    # Открываем файл в режиме записи
    with open(file_name, 'w', encoding='UTF-8') as file:
        # Итерируемся по количеству слов
        for i in range(1, word_count + 1):
            # Формируем строку с номером слова
            word = f"Какое-то слово № {i}"

            # Записываем слово в файл
            file.write(word + '\n')

            # Приостанавливаем выполнение на 0.1 секунды
            sleep(0.1)

    # Выводим сообщение о завершении записи в файл
    print(f"Завершилась запись в файл {file_name}")


def main():
    # Засекаем начальное время для функций
    start_time_func = time.time()

    # Последовательный вызов функций записи
    print("Последовательное выполнение:")
    write_words(10, "example1.txt")
    write_words(30, "example2.txt")
    write_words(200, "example3.txt")
    write_words(100, "example4.txt")

    # Вычисляем и выводим время выполнения функций
    end_time_func = time.time()
    func_duration = end_time_func - start_time_func
    print(f"Время работы функций: {func_duration:.2f} секунд")

    # Засекаем начальное время для потоков
    start_time_threads = time.time()

    # Список аргументов для потоков
    thread_args = [
        (10, "example5.txt"),
        (30, "example6.txt"),
        (200, "example7.txt"),
        (100, "example8.txt")
    ]

    # Создаем список потоков
    threads = []

    # Создаем и запускаем потоки
    print("\nПараллельное выполнение:")
    for args in thread_args:
        # Создаем поток с целевой функцией write_words
        thread = threading.Thread(target=write_words, args=args)
        threads.append(thread)
        # Запускаем поток
        thread.start()

    # Ожидаем завершения всех потоков
    for thread in threads:
        thread.join()

    # Вычисляем и выводим время выполнения потоков
    end_time_threads = time.time()
    threads_duration = end_time_threads - start_time_threads
    print(f"Время работы потоков: {threads_duration:.2f} секунд")


# Точка входа в программу
if __name__ == "__main__":
    # Запускаем основную функцию
    main()