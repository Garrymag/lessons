import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._coords = [0, 0, 0]  # Изначальные координаты
        self.speed = speed  # Скорость передвижения

    def move(self, dx, dy, dz):
        # Изменяем координаты с учетом скорости
        self._coords[0] += dx * self.speed
        self._coords[1] += dy * self.speed

        # Проверяем изменение координаты z
        if self._coords[2] + dz * self.speed < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._coords[2] += dz * self.speed

    def get_coords(self):
        # Возвращаем координаты в заданном формате
        print(f"X: {self._coords[0]} Y: {self._coords[1]} Z: {self._coords[2]}")

    def attack(self):
        # Проверка степени опасности для атаки
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):
        # Возвращаем звук, если он установлен
        if self.sound:
            print(self.sound)


class Bird(Animal):
    beak = True  # Наличие клюва

    def lay_eggs(self):
        # Генерация случайного количества яиц от 1 до 4
        eggs = random.randint(1, 4)
        print(f"Here are(is) {eggs} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3  # Степень опасности для водных животных

    def dive_in(self, dz):
        # Уменьшаем координату z, беря модуль dz
        dz = abs(dz)
        if self._coords[2] - dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._coords[2] -= dz
            self.speed /= 2  # Уменьшаем скорость в 2 раза


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8  # Степень опасности для ядовитых животных


class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = "Click-click-click"  # Звук утконоса

    def __init__(self, speed):
        super().__init__(speed)  # Инициализация родительского класса


# Пример работы программы
def main():
    db = Duckbill(10)  # Создаем утконоса с заданной скоростью

    # Проверка состояния утконоса
    print(db.live)  # Должно быть True
    print(db.beak)  # Должно быть True

    # Утконос издает звук
    db.speak()

    # Проверяем степень опасности и атаку
    db.attack()

    # Утконос передвигается
    db.move(1, 2, 3)  # Передвижение по координатам
    db.get_coords()  # Получаем текущие координаты

    # Утконос ныряет
    db.dive_in(6)  # Пытаемся нырнуть
    db.get_coords()  # Получаем новые координаты после ныряния

    # Утконос откладывает яйца
    db.lay_eggs()


# Точка входа в программу
if __name__ == "__main__":
    main()