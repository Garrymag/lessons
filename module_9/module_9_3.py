first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Первый генератор - разница длин строк
first_result = (abs(len(a) - len(b)) for a, b in zip(first, second) if len(a) != len(b))

# Второй генератор - сравнение длин строк
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# Проверка
print(list(first_result))
print(list(second_result))
