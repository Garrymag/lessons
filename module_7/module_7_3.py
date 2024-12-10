class WordsFinder:
    def __init__(self, *file_names):
        """
        Конструктор класса, принимающий произвольное количество имен файлов

        :param file_names: Названия файлов для поиска
        """
        # Сохраняем имена файлов как список или кортеж
        self.file_names = file_names

    def get_all_words(self):
        """
        Метод для получения всех слов из файлов

        :return: Словарь со словами из каждого файла
        """
        # Словарь для хранения слов из файлов
        all_words = {}

        # Список пунктуации для удаления
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

        # Перебираем файлы
        for file_name in self.file_names:
            try:
                # Открываем файл с кодировкой utf-8
                with open(file_name, 'r', encoding='utf-8') as file:
                    # Читаем все строки файла
                    text = file.read().lower()

                    # Удаляем пунктуацию
                    for punct in punctuation:
                        text = text.replace(punct, '')

                    # Разбиваем текст на слова
                    words = text.split()

                    # Сохраняем список слов для файла
                    all_words[file_name] = words

            except FileNotFoundError:
                print(f"Файл {file_name} не найден")

        return all_words

    def find(self, word):
        """
        Метод для поиска первого вхождения слова

        :param word: Искомое слово
        :return: Словарь с позицией первого вхождения слова
        """
        # Получаем все слова
        all_words = self.get_all_words()

        # Словарь для хранения результатов
        result = {}

        # Перебираем файлы и их слова
        for name, words in all_words.items():
            # Приводим искомое слово к нижнему регистру
            word = word.lower()

            # Ищем первое вхождение слова
            try:
                position = words.index(word) + 1
                result[name] = position
            except ValueError:
                # Если слово не найдено, пропускаем файл
                pass

        return result

    def count(self, word):
        """
        Метод для подсчета количества вхождений слова

        :param word: Искомое слово
        :return: Словарь с количеством вхождений слова
        """
        # Получаем все слова
        all_words = self.get_all_words()

        # Словарь для хранения результатов
        result = {}

        # Перебираем файлы и их слова
        for name, words in all_words.items():
            # Приводим искомое слово к нижнему регистру
            word = word.lower()

            # Считаем количество вхождений слова
            word_count = words.count(word)

            # Если слово встречается, добавляем в результат
            if word_count > 0:
                result[name] = word_count

        return result


# Примеры использования
def main():
    # Пример 1
    print("Пример 1:")
    finder2 = WordsFinder('test_file.txt')
    print(finder2.get_all_words())  # Все слова
    print(finder2.find('TEXT'))  # 3 слово по счёту
    print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

    # Пример 2
    print("\nПример 2:")
    finder1 = WordsFinder("Mother Goose - Monday’s Child.txt")
    print(finder1.get_all_words())
    print(finder1.find('Child'))
    print(finder1.count('Child'))

    # Пример 3
    print("\nПример 3:")
    finder1 = WordsFinder('Rudyard Kipling - If.txt', )
    print(finder1.get_all_words())
    print(finder1.find('if'))
    print(finder1.count('if'))

    # Пример 4
    print("\nПример 4:")
    finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
    print(finder1.get_all_words())
    print(finder1.find('captain'))
    print(finder1.count('captain'))

# Запуск примеров
if __name__ == "__main__":
    main()
