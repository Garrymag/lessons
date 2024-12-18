#Определение класса исключения для некорректного VIN номера
class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message  # Сообщение, которое будет выводиться при выбрасывании исключения

# Определение класса исключения для некорректных автомобильных номеров
class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message  # Сообщение, которое будет выводиться при выбрасывании исключения

# Основной класс для автомобиля
class Car:
    def __init__(self, model, vin, numbers):
        self.model = model  # Название модели автомобиля
        # Проверка и установка VIN номера
        if self.__is_valid_vin(vin):
            self.__vin = vin  # Приватный атрибут VIN номера
        # Проверка и установка номера автомобиля
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers  # Приватный атрибут номера автомобиля

    # Приватный метод для проверки корректности VIN номера
    def __is_valid_vin(self, vin_number):
        # Проверка, является ли VIN номер целым числом
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')  # Выбрасываем исключение, если тип неверный
        # Проверка, входит ли VIN номер в допустимый диапазон
        if not 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')  # Выбрасываем исключение, если диапазон неверный
        return True  # Возвращаем True, если проверки прошли успешно

    # Приватный метод для проверки корректности номера автомобиля
    def __is_valid_numbers(self, numbers):
        # Проверка, является ли номер строкой
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')  # Выбрасываем исключение, если тип неверный
        # Проверка длины номера автомобиля
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')  # Выбрасываем исключение, если длина неверная
        return True  # Возвращаем True, если проверки прошли успешно


# Пример создания объекта автомобиля с корректными данными
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)  # Выводим сообщение об ошибке, если возникло исключение IncorrectVinNumber
except IncorrectCarNumbers as exc:
    print(exc.message)  # Выводим сообщение об ошибке, если возникло исключение IncorrectCarNumbers
else:
    print(f'{first.model} успешно создан')  # Если объект успешно создан, выводим сообщение

# Пример создания объекта автомобиля с некорректным VIN номером
try:
    second = Car('Model2', 300, 'т001тр')  # VIN номер вне допустимого диапазона
except IncorrectVinNumber as exc:
    print(exc.message)  # Выводим сообщение об ошибке
except IncorrectCarNumbers as exc:
    print(exc.message)  # Выводим сообщение об ошибке
else:
    print(f'{second.model} успешно создан')

# Пример создания объекта автомобиля с некорректной длиной номера
try:
    third = Car('Model3', 2020202, 'нет номера')  # Номер менее 6 символов
except IncorrectVinNumber as exc:
    print(exc.message)  # Выводим сообщение об ошибке
except IncorrectCarNumbers as exc:
    print(exc.message)  # Выводим сообщение об ошибке
else:
    print(f'{third.model} успешно создан')