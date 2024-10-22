# https://github.com/Garrymag/lessons/blob/master/module_1_5.py
# Создание переменной immutable_var и присвоение ей кортежа
immutable_var = (1, 'строка', 3.14, True, None)
# Вывод кортежа immutable_var на экран
print("Кортеж immutable_var:", immutable_var)
# Код для попытки изменения элемента кортежа напишем в конце, чтоб ошибка не мешала
# Создание переменной mutable_list и присвоение ей списка
mutable_list = [1, 'строка', 3.14, True, None]
# Изменение первого элемента списка mutable_list
mutable_list[0] = 10
# Изменение последнего элемента списка mutable_list
mutable_list[-1] = 'новое значение'
# Вывод измененного списка mutable_list на экран
print("Измененный список mutable_list:", mutable_list)
# Попытка изменить первый элемент кортежа immutable_var
immutable_var[0] = 10