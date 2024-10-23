# https://github.com/Garrymag/lessons/blob/master/module_1_7.py

# Данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Преобразуем множество в список для упорядочивания
students_list = list(students)
# И сортируем его
students_list.sort()

# Создаем пустой словарь
average_grades = {}
# Заполняем словарь именами студентов и их средними баллами
average_grades[students_list[0]] = sum(grades[0]) / len(grades[0])
average_grades[students_list[1]] = sum(grades[1]) / len(grades[1])
average_grades[students_list[2]] = sum(grades[2]) / len(grades[2])
average_grades[students_list[3]] = sum(grades[3]) / len(grades[3])
average_grades[students_list[4]] = sum(grades[4]) / len(grades[4])

# Выводим итоговый словарь
print(average_grades)