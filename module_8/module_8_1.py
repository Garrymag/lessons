def add_everything_up(a, b):
    try:
        # Пробуем сложить значения
        return a + b
    except TypeError:
        # Если получили TypeError (разные типы данных), 
        # возвращаем строковое представление обоих значений
        return str(a) + str(b)

# Тесты
print(add_everything_up(123.456, 'строка'))  # -> '123.456строка'
print(add_everything_up('яблоко', 4215))     # -> 'яблоко4215'
print(add_everything_up(123.456, 7))         # -> 130.456
print(add_everything_up('hello', 'world'))   # -> 'helloworld'