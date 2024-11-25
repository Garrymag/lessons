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


# Создаем объекты класса House
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# Пример использования метода __str__
print(h1)
print(h2)

# Пример использования метода __len__
print(len(h1))
print(len(h2))