# https://github.com/Garrymag/lessons/blob/master/module_2/module_2_hard.py

# Пароль будем формировать в функции
def generate_password(n):
    if not (3 <= n <= 20): # Проверка диапазона аргумента
        return "Число должно быть от 3 до 20"
    result = ""
    # Проходим по всем числам от 1 до 20
    for i in range(1, 21):
        for j in range(i + 1, 21):  # j начинается с i + 1 для уникальности пар
            pair_sum = i + j
            if n % pair_sum == 0:  # Проверяем кратность
                result += f"{i}{j}"  # Добавляем пару в результат
    return result

# Выведем сразу все пароли
for number in range(3, 22):
    password = generate_password(number)
    print(f"Пароль для числа {number} - {password}")