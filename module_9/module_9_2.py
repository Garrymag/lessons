# Данные списки
first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Сборка списка длин строк из first_strings, где длина строк >= 5
first_result = [len(s) for s in first_strings if len(s) >= 5]

# Сборка списка пар слов (кортежей) одинаковой длины между first_strings и second_strings
second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]

# Сборка словаря с ключом - строка, значением - длина строки из объединенных списков
third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}

# Пример выполнения кода
print(first_result)
print(second_result)
print(third_result)