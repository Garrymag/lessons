def custom_write(file_name, strings):
    """
    Записывает строки в файл и возвращает словарь с позициями строк.

    :param file_name: Имя файла для записи
    :param strings: Список строк для записи
    :return: Словарь с позициями строк
    """
    # Словарь для хранения позиций и строк
    strings_positions = {}

    # Открываем файл в режиме записи с кодировкой utf-8
    file = open(file_name, 'w', encoding='utf-8')

    # Счетчик для нумерации строк
    line_number = 1

    # Перебираем строки
    for string in strings:
        # Запоминаем текущую позицию в файле перед записью
        current_position = file.tell()

        # Записываем строку с переводом строки
        file.write(string + '\n')

        # Сохраняем информацию в словарь
        strings_positions[(line_number, current_position)] = string

        # Увеличиваем номер строки
        line_number += 1

    # Закрываем файл
    file.close()

    return strings_positions


# Пример использования
if __name__ == "__main__":
    info = [
        'Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!'
    ]

    result = custom_write('test.txt', info)

    # Вывод результата
    for elem in result.items():
        print(elem)
