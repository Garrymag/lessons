# 1. Создаем функцию с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(f"a = {a}, b = {b}, c = {c}")

# Демонстрация различных вызовов:
print("1. Вызовы функции с разными параметрами:")
print_params()  # все значения по умолчанию
print_params(10)  # изменяем только a
print_params(b=25)  # изменяем только b
print_params(c=[1,2,3])  # изменяем только c

# 2. Распаковка параметров
print("\n2. Распаковка параметров из списка и словаря:")
values_list = [100, "test", False]
values_dict = {'a': 200, 'b': "python", 'c': [1,2,3]}

print("Распаковка списка:")
print_params(*values_list)
print("Распаковка словаря:")
print_params(**values_dict)

# 3. Распаковка + отдельные параметры
print("\n3. Распаковка списка + дополнительный параметр:")
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
