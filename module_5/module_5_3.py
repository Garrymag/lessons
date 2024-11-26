class House:
    def __init__(self, name, number_of_floors):
        # Сохраняем название дома как атрибут объекта
        self.name = name
        # Сохраняем количество этажей как атрибут объекта
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        # Проверяем, является ли указанный этаж корректным
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            # Если этаж корректный, выводим все этажи от 1 до указанного
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        # Возвращаем количество этажей
        return self.number_of_floors

    def __str__(self):
        # Возвращаем строковое представление объекта
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    # Методы сравнения
    def __eq__(self, other):
        # Проверяем, что other является объектом House
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        # Если other не объект House, возвращаем False
        return False

    def __lt__(self, other):
        # Проверяем, что other является объектом House или числом
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        # Если other число, сравниваем с ним
        if isinstance(other, int):
            return self.number_of_floors < other
        return NotImplemented

    def __le__(self, other):
        # Проверяем, что other является объектом House или числом
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        # Если other число, сравниваем с ним
        if isinstance(other, int):
            return self.number_of_floors <= other
        return NotImplemented

    def __gt__(self, other):
        # Проверяем, что other является объектом House или числом
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        # Если other число, сравниваем с ним
        if isinstance(other, int):
            return self.number_of_floors > other
        return NotImplemented

    def __ge__(self, other):
        # Проверяем, что other является объектом House или числом
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        # Если other число, сравниваем с ним
        if isinstance(other, int):
            return self.number_of_floors >= other
        return NotImplemented

    def __ne__(self, other):
        # Проверяем, что other является объектом House
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        # Если other не объект House, возвращаем False
        return False

    # Методы арифметических операций
    def __add__(self, value):
        # Проверяем, что value является числом
        if isinstance(value, int):
            # Создаем новый объект с тем же именем и увеличенным кол-вом этажей
            return House(self.name, self.number_of_floors + value)
        return NotImplemented

    def __radd__(self, value):
        # Вызываем __add__, так как сложение коммутативно
        return self.__add__(value)

    def __iadd__(self, value):
        # Увеличиваем количество этажей текущего объекта
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        return NotImplemented


# Пример использования
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)  # Название: ЖК Акация, кол-во этажей: 20

print(h1 == h2)  # False

h1 = h1 + 10  # __add__
print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 20
print(h1 == h2)  # True

h1 += 10  # __iadd__
print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 30

h2 = 10 + h2  # __radd__
print(h2)  # Название: ЖК Акация, кол-во этажей: 30

print(h1 > h2)  # False
print(h1 >= h2)  # True
print(h1 < h2)  # False
print(h1 <= h2)  # True
print(h1 != h2)  # False