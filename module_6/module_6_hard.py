import math


class Figure:
    """Базовый класс для геометрических фигур"""

    # Количество сторон по умолчанию
    sides_count = 0

    def __init__(self, color, *sides):
        """
        Инициализация фигуры

        :param color: кортеж цвета RGB
        :param sides: стороны фигуры
        """
        # Публичный атрибут заливки
        self.filled = False

        # Приватный атрибут цвета
        self.__color = list(color)

        # Приватный атрибут сторон
        if len(sides) == self.sides_count:
            # Если передано корректное количество сторон
            self.__sides = list(sides)
        else:
            # Иначе создаем список из единиц нужной длины
            self.__sides = [1] * self.sides_count

    def __is_valid_color(self, r, g, b):
        """
        Проверка корректности цвета

        :return: True если цвет корректен, иначе False
        """
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def __is_valid_sides(self, *sides):
        """
        Проверка корректности сторон

        :return: True если стороны корректны, иначе False
        """
        return (len(sides) == self.sides_count and
                all(isinstance(side, int) and side > 0 for side in sides))

    def get_color(self):
        """Получение текущего цвета"""
        return self.__color

    def set_color(self, r, g, b):
        """
        Установка нового цвета

        :param r: красный канал
        :param g: зеленый канал
        :param b: синий канал
        """
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def get_sides(self):
        """Получение списка сторон"""
        return self.__sides

    def set_sides(self, *new_sides):
        """
        Установка новых сторон

        :param new_sides: новые значения сторон
        """
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def __len__(self):
        """
        Возвращает периметр фигуры

        :return: сумма всех сторон
        """
        return sum(self.__sides)


class Circle(Figure):
    """Класс круга"""
    # Количество сторон для круга
    sides_count = 1

    def __init__(self, color, *sides):
        """
        Инициализация круга

        :param color: цвет круга
        :param sides: длина окружности или радиус
        """
        super().__init__(color, *sides)

        # Расчет радиуса
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        """
        Расчет площади круга

        :return: площадь круга
        """
        return math.pi * self.__radius ** 2


class Triangle(Figure):
    """Класс треугольника"""
    # Количество сторон для треугольника
    sides_count = 3

    def get_square(self):
        """
        Расчет площади треугольника по формуле Герона

        :return: площадь треугольника
        """
        # Получаем стороны
        a, b, c = self.get_sides()

        # Полупериметр
        p = (a + b + c) / 2

        # Формула Герона
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

class Cube(Figure):
    """Класс куба"""
    # Количество сторон для куба
    sides_count = 12

    def __init__(self, color, *sides):
        """
        Инициализация куба

        :param color: цвет куба
        :param sides: сторона куба
        """
        # Если передана одна сторона, создаем список из 12 одинаковых сторон
        if len(sides) == 1:
            sides = [sides[0]] * self.sides_count

        # Вызываем родительский конструктор
        super().__init__(color, *sides)

    def get_volume(self):
        """
        Расчет объема куба

        :return: объем куба
        """
        # Берем первую сторону как ребро куба
        side = self.get_sides()[0]
        return side ** 3


# Демонстрация работы классов
def main():
    # Создаем круг
    circle1 = Circle((200, 200, 100), 10)

    # Создаем куб
    cube1 = Cube((222, 35, 130), 6)

    # Создаем треугольник

    triangle1 = Triangle((50, 60, 70), 3)

    # Проверка изменения цветов
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())

    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка изменения сторон
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())

    triangle1.set_sides(12, 12, 3)

    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра круга
    print(len(circle1))

    # Проверка объема куба
    print(cube1.get_volume())

# Дополнительные проверки
    triangle1 = Triangle((100, 200, 150), 3, 4, 5)
    print("Triangle sides:", triangle1.get_sides())  # Ожидается: [3, 4, 5]
    print("Triangle area:", triangle1.get_square())  # Ожидается: 6.0

    circle2 = Circle((255, 255, 255), 10)  # Создание круга
    print("Circle area:", circle2.get_square())  # Ожидается: площадь круга

    cube2 = Cube((10, 20, 30), 5)  # Создание куба
    print("Cube volume:", cube2.get_volume())  # Ожидается: 125 (5*5*5)

# Точка входа в программу
if __name__ == "__main__":
    main()