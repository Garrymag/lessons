# https://github.com/Garrymag/lessons/blob/master/module_2/module_2_4.py

# Исходный список чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Создаем пустые списки для простых и не простых чисел
primes = []
not_primes = []

# Перебираем список numbers
for num in numbers:
    # Пропускаем 1
    if num < 2:
        continue

    # Предполагаем, что число простое
    is_prime = True

    # Проверяем делители от 2 до num - 1
    for i in range(2, num):
        if num % i == 0:  # Если есть делитель
            is_prime = False  # Число не простое
            break  # Выходим из цикла

    # Добавляем число в соответствующий список
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

# Выводим списки на экран
print("Простые числа:", primes)
print("Непростые числа:", not_primes)