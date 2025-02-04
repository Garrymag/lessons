# https://github.com/Garrymag/lessons/blob/master/module_1_6.py

# Работа со словарями
# Создаем словарь
my_dict = {
    "Имя": "Алексей",
    "Год рождения": 1990,
    "Город": "Москва"
}

print(my_dict)  # Выводим словарь

print(my_dict.get("Имя"))  # Существующий ключ
print(my_dict.get("Возраст", "Ключ не найден"))  # Отсутствующий ключ

my_dict["Профессия"] = "Инженер"
my_dict["Хобби"] = "Чтение"

removed_value = my_dict.pop("Город")  # Удаляем "Город"
print(removed_value)  # Выводим удаленное значение

print(my_dict)  # Выводим измененный словарь

# Работа с множествами
my_set = {1, "текст", 3.14, 1, "текст", 2}  # Повторяющиеся значения будут удалены
print(my_set)  # Выводим множество

my_set.add(42)  # Добавляем новый элемент
my_set.add("новый элемент")  # Добавляем еще один новый элемент

my_set.remove(1)  # Удаляем элемент 1
print(my_set)  # Выводим измененное множество
