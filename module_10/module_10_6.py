import time
import multiprocessing

def read_info(name):
    all_data = []
    # Инициализируем пустой список для хранения данных из файла
    with open(name, 'r') as file:
        # Открываем указанный файл в режиме чтения, используя менеджер контекста, чтобы гарантировать его правильное закрытие после чтения
        while True:
            # Запускаем бесконечный цикл для чтения файла построчно
            line = file.readline()
            # Читаем одну строку из файла
            if not line:
                # Если строка не прочитана (конец файла), выходим из цикла
                break
            all_data.append(line)
            # Добавляем прочитанную строку в список all_data

filenames = [f'./file {number}.txt' for number in range(1, 5)]
# Создаем список имен файлов от './file 1.txt' до './file 4.txt' с помощью списочного включения

# Линейное выполнение
start_time = time.time()
# Записываем время начала линейного выполнения
for filename in filenames:
    read_info(filename)
    # Вызываем read_info для каждого имени файла в списке последовательно
end_time = time.time()
# Записываем время окончания после обработки всех файлов последовательно
print(f"Linear execution time: {end_time - start_time}")
# Выводим общее время, затраченное на линейное выполнение

# Выполнение с multiprocessing
if __name__ == '__main__':
    # Защищаем точку входа скрипта, чтобы гарантировать безопасное создание процессов
    start_time = time.time()
    # Записываем время начала выполнения с использованием multiprocessing
    with multiprocessing.Pool() as pool:
        # Создаем пул рабочих процессов с использованием менеджера контекста для обеспечения правильного закрытия пула
        pool.map(read_info, filenames)
        # Распределяем вызовы read_info по рабочим процессам в пуле
    end_time = time.time()
    # Записываем время окончания после обработки всех файлов параллельно
    print(f"Multiprocessing execution time: {end_time - start_time}")
    # Выводим общее время, затраченное на выполнение с multiprocessing