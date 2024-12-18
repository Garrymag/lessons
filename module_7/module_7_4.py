# Входные данные
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 18015.2
team2_time = 2153.31451
tasks_total = 82
time_avg = 350.4

# Определение результата соревнования
if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'


# Форматирование с использованием %
def percent_formatting():
    print("Использование %:")

    # Форматирование с количеством участников первой команды
    print("В команде Мастера кода участников: %d !" % team1_num)

    # Форматирование с количеством участников в обеих командах
    print("Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num))


# Форматирование с использованием .format()
def format_method():
    print("\nИспользование .format():")

    # Форматирование количества решённых задач командой 2
    print("Команда Волшебники данных решила задач: {} !".format(score_2))

    # Форматирование времени решения задач командой 2
    print("Волшебники данных решили задачи за {:.1f} с !".format(team1_time))


# Форматирование с использованием f-строк
def f_string_formatting():
    print("\nИспользование f-строк:")

    # Форматирование количества решённых задач по командам
    print(f"Команды решили {score_1} и {score_2} задач.")

    # Форматирование результата соревнования
    print(f"Результат битвы: {challenge_result}")

    # Форматирование количества задач и среднего времени решения
    print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!")


# Вызов функций форматирования
def main():
    percent_formatting()
    format_method()
    f_string_formatting()


# Запуск программы
if __name__ == "__main__":
    main()