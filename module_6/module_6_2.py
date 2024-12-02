class Vehicle:
    # Список допустимых цветов (атрибут класса)
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        """
        Инициализация объекта Vehicle

        :param owner: владелец транспорта (может меняться)
        :param model: модель транспорта (не может меняться)
        :param color: цвет транспорта
        :param engine_power: мощность двигателя
        """
        # Публичный атрибут владельца (может меняться)
        self.owner = owner

        # Приватные атрибуты (защищены от прямого изменения)
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        """Возвращает информацию о модели"""
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        """Возвращает информацию о мощности двигателя"""
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        """Возвращает информацию о цвете"""
        return f"Цвет: {self.__color}"

    def print_info(self):
        """Печатает полную информацию о транспорте"""
        # Вызываем методы получения информации
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color):
        """
        Метод смены цвета с проверкой допустимых вариантов

        :param new_color: новый цвет для транспорта
        """
        # Приводим цвета к нижнему регистру для сравнения
        if new_color.lower() in [color.lower() for color in self.__COLOR_VARIANTS]:
            # Если цвет допустим - меняем
            self.__color = new_color
        else:
            # Если цвет не допустим - выводим сообщение
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    # Константа количества пассажиров для седана
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, color, engine_power):
        """
        Инициализация объекта Sedan
        Вызывает конструктор родительского класса
        """
        # Используем super() для вызова конструктора Vehicle
        super().__init__(owner, model, color, engine_power)


# Демонстрация работы классов
def main():
    # Создаем объект седана
    vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

    # Печатаем изначальную информацию
    print("Изначальные свойства:")
    vehicle1.print_info()
    print("\n")

    # Пытаемся изменить цвет на недопустимый
    print("Попытка изменить цвет на недопустимый:")
    vehicle1.set_color('Pink')
    print("\n")

    # Меняем цвет на допустимый
    print("Изменение цвета на допустимый:")
    vehicle1.set_color('BLACK')

    # Меняем владельца
    vehicle1.owner = 'Vasyok'

    # Печатаем измененную информацию
    print("\nИзмененные свойства:")
    vehicle1.print_info()


# Точка входа в программу
if __name__ == "__main__":
    main()