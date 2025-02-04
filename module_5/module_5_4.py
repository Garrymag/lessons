class House:
    # Класcовый атрибут для хранения истории созданных домов
    houses_history = []

    def __new__(cls, *args, **kwargs):
        # Метод __new__ вызывается перед созданием объекта

        # Добавляем название дома в историю
        # args[0] - первый позиционный аргумент (название дома)
        if args:
            cls.houses_history.append(args[0])

        # Создаем и возвращаем новый объект
        return super().__new__(cls)

    def __del__(self):
        # Метод вызывается при удалении объекта
        print(f"{self.name} снесён, но он останется в истории")

    def __init__(self, name, number_of_floors):
        # Конструктор класса House
        # name - название дома
        # number_of_floors - количество этажей в доме
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        # Метод для перехода на указанный этаж
        # new_floor - этаж, на который хотим перейти
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")  # Если этаж вне диапазона
        else:
            # Если этаж корректный, выводим все этажи от 1 до указанного
            for floor in range(1, new_floor + 1):
                print(floor)

    def __len__(self):
        # Метод возвращает количество этажей в доме
        return self.number_of_floors

    def __str__(self):
        # Метод возвращает строковое представление объекта House
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    # Методы сравнения
    def __eq__(self, other):
        # Метод для проверки на равенство
        # Если other - объект House, сравниваем количество этажей
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        # Если other - целое число, сравниваем с количеством этажей
        elif isinstance(other, int):
            return self.number_of_floors == other
        # Если other не поддерживаемый тип, возвращаем NotImplemented
        return NotImplemented

    def __lt__(self, other):
        # Метод для проверки, меньше ли количество этажей
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other
        return NotImplemented

    def __le__(self, other):
        # Метод для проверки, меньше или равно ли количество этажей
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors <= other
        return NotImplemented

    def __gt__(self, other):
        # Метод для проверки, больше ли количество этажей
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors > other
        return NotImplemented

    def __ge__(self, other):
        # Метод для проверки, больше или равно ли количество этажей
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors >= other
        return NotImplemented

    def __ne__(self, other):
        # Метод для проверки на неравенство
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors != other
        return NotImplemented

    # Методы арифметических операций
    def __add__(self, value):
        # Метод для сложения количества этажей с целым числом
        if isinstance(value, int):
            # Возвращаем объект House с увеличенным количеством этажей
            self.number_of_floors += value
            return self
        return NotImplemented

    def __radd__(self, value):
        # Метод для сложения, когда объект House находится справа
        # Вызываем __add__
        return self.__add__(value)

    def __iadd__(self, value):
        # Метод для увеличения количества этажей текущего объекта
        # Вызываем __add__
        return self.__add__(value)

# Создаем объекты
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)  # ['ЖК Эльбрус']

h2 = House('ЖК Акация', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация']

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)  # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']

# Удаление объектов
del h2
del h3

print(House.houses_history)