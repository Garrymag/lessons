def single_root_words(root_word, *other_words):
    """
    Функция для выбора слов из other_words, которые содержат root_word
    или наоборот, root_word содержит эти слова. Проверка производится без учета регистра символов.

    :param root_word: Корневое слово (строка).
    :param other_words: Неограниченное количество слов для проверки.
    :return: Список слов, соответствующих условию.
    """

    # Создаём пустой список для хранения слов, удовлетворяющих условию
    same_words = []

    # Преобразуем root_word в нижний регистр для корректного сравнения без учета регистра
    root_lower = root_word.lower()

    # Проходимся по каждому слову в списке other_words
    for word in other_words:
        # Преобразуем текущие слово в нижний регистр
        word_lower = word.lower()

        # Проверяем, содержится ли root_word в текущем слове или текущее слово в root_word
        if root_lower in word_lower or word_lower in root_lower:
            # Если условие выполняется, добавляем оригинальное слово (с исходным регистром) в список same_words
            same_words.append(word)

    # Возвращаем сформированный список слов
    return same_words

# Первый пример
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')

# Второй пример
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Вывод результатов на экран
print(result1)
print(result2)
