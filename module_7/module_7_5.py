import os
import time


def explore_directory(directory="."):
    """
    Функция для исследования файлов в директории

    :param directory: Путь к директории (по умолчанию текущая)
    """
    # Проходим по всем подпапкам и файлам с помощью os.walk
    for root, dirs, files in os.walk(directory):
        # Перебираем каждый файл
        for file in files:
            # Формируем полный путь к файлу с помощью os.path.join
            filepath = os.path.join(root, file)

            # Получаем время последней модификации файла
            filetime = os.path.getmtime(filepath)

            # Форматируем время в удобочитаемый формат
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

            # Получаем размер файла
            filesize = os.path.getsize(filepath)

            # Получаем родительскую директорию
            parent_dir = os.path.dirname(filepath)

            # Выводим информацию о файле
            print(f'Обнаружен файл: {file}, '
                  f'\nПуть: {filepath}, '
                  f'\nРазмер: {filesize} байт, '
                  f'\nВремя изменения: {formatted_time}, '
                  f'\nРодительская директория: {parent_dir}\n\n')


def main():
    # По умолчанию исследуем текущую директорию
    explore_directory(".")


# Запуск программы
if __name__ == "__main__":
    main()