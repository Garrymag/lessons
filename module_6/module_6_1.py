# Базовый класс для всех животных
class Animal:
    def __init__(self, name):
        # Имя каждого животного
        self.name = name

        # Статус жизни: по умолчанию животное живое
        self.alive = True

        # Статус сытости: по умолчанию голодное
        self.fed = False
    def eat(self, food):
        # Метод принимает объект растения в качестве аргумента

        # Проверяем, съедобно ли растение
        if food.edible:
            # Если съедобно - выводим сообщение о съедении
            print(f"{self.name} съел {food.name}")

            # Меняем статус сытости на "сыт"
            self.fed = True
        else:
            # Если несъедобно - выводим сообщение и убиваем животное
            print(f"{self.name} не стал есть {food.name}")

            # Меняем статус жизни на "мертв"
            self.alive = False

# Базовый класс для всех растений
class Plant:
    def __init__(self, name):
        # Имя каждого растения
        self.name = name

        # По умолчанию растение не съедобно
        self.edible = False


# Класс млекопитающих, наследуется от Animal
class Mammal(Animal):
    # Явно не добавляем никаких методов
    # Наследует все свойства от Animal
    pass


# Класс хищников, также наследуется от Animal
class Predator(Animal):
    # Явно не добавляем никаких методов
    # Наследует все свойства от Animal
    pass

# Класс цветов, наследуется от Plant
class Flower(Plant):
    # Явно не добавляем никаких методов
    # Наследует все свойства от Plant, включая edible = False
    pass


# Класс фруктов, наследуется от Plant
class Fruit(Plant):
    def __init__(self, name):
        # Вызываем конструктор родительского класса
        super().__init__(name)

        # Переопределяем свойство edible для фруктов
        # Теперь фрукты считаются съедобными
        self.edible = True


# Демонстрация работы классов
def main():
    # Создаем объекты классов

    # Хищник с уникальным именем
    a1 = Predator('Волк с Уолл-Стрит')

    # Млекопитающее с уникальным именем
    a2 = Mammal('Хатико')

    # Несъедобный цветок
    p1 = Flower('Цветик семицветик')

    # Съедобный фрукт
    p2 = Fruit('Заводной апельсин')

    # Демонстрация начальных свойств
    print(a1.name)  # Имя первого животного
    print(p1.name)  # Имя первого растения

    print(a1.alive)  # Статус жизни первого животного
    print(a2.fed)  # Статус сытости второго животного

    # Попытка съесть несъедобный цветок хищником
    a1.eat(p1)

    # Попытка съесть съедобный фрукт млекопитающим
    a2.eat(p2)

    # Проверка изменившихся статусов
    print(a1.alive)  # Хищник должен умереть
    print(a2.fed)  # Млекопитающее должно насытиться


# Запуск основной функции
if __name__ == "__main__":
    main()