import math

class Figure:
    sides_count = 0  # Класс атрибут для подсчета сторон

    def __init__(self, color, *sides):
        self.__color = list(color) if self.__is_valid_color(*color) else [0, 0, 0]  # Установка цвета с проверкой
        self.filled = False  # Публичный атрибут, обозначающий заполненность
        # Проверяем количество сторон, если их не достаточно, создаем список с единицами
        if self.__is_valid_sides(*sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count  # Создаем массив с единицами

    # Геттер для цвета
    def get_color(self):
        return self.__color.copy()

    # Сеттер для цвета с проверкой валидности
    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    # Внутренний метод для проверки валидности цвета
    def __is_valid_color(self, r, g, b):
        return all(isinstance(c, int) and 0 <= c <= 255 for c in (r, g, b))

    # Внутренний метод для проверки валидности сторон
    def __is_valid_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            return False
        return all(isinstance(side, int) and side > 0 for side in new_sides)

    # Геттер для сторон
    def get_sides(self):
        return self.__sides.copy()

    # Сеттер для сторон с проверкой валидности
    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    # Периметр фигуры
    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1  # У круга одна сторона

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        # Рассчитываем радиус исходя из длины окружности
        circumference = len(self)
        self.__radius = circumference / (2 * math.pi)  # Радиус

    # Метод для получения площади круга
    def get_square(self):
        return math.pi * (self.__radius ** 2)

    # Геттер для радиуса
    def get_radius(self):
        return self.__radius

class Triangle(Figure):
    sides_count = 3  # У треугольника три стороны

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    # Метод для получения площади треугольника по формуле Герона
    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

class Cube(Figure):
    sides_count = 12  # У куба 12 рёбер

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(self.get_sides()) == 1:  # Если передали одну сторону
            side_length = self.get_sides()[0]
            self.__sides = [side_length] * self.sides_count  # Заполняем 12 одинаковыми сторонами
        else:
            self.__sides = [1] * self.sides_count  # По умолчанию

    # Переопределяем метод для получения объёма куба
    def get_volume(self):
        if len(set(self.__sides)) == 1:  # Проверяем, что все стороны одинаковы
            return self.__sides[0] ** 3
        return 0  # Объём 0, если стороны не одинаковы

# Код для проверки:

if __name__ == "__main__":
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())  # Ожидается: [55, 66, 77]

    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())  # Ожидается: [222, 35, 130]

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())  # Ожидается: [6, 6, 6, ..., 6] (12)

    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())  # Ожидается: [15]

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))  # Ожидается: 15

    # Проверка объёма (куба):
    print(cube1.get_volume())  # Ожидается: 216 (6*6*6)

    # Дополнительные проверки
    triangle1 = Triangle((100, 200, 150), 3, 4, 5)
    print("Triangle sides:", triangle1.get_sides())  # Ожидается: [3, 4, 5]
    print("Triangle area:", triangle1.get_square())  # Ожидается: 6.0

    circle2 = Circle((255, 255, 255), 10)  # Создание круга
    print("Circle area:", circle2.get_square())  # Ожидается: площадь круга

    cube2 = Cube((10, 20, 30), 5)  # Создание куба
    print("Cube volume:", cube2.get_volume())  # Ожидается: 125 (5*5*5)