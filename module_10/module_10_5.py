import threading
from queue import Queue
import random
import time

# Класс Table представляет стол в кафе
class Table:
    def __init__(self, number):
        self.number = number  # Номер стола
        self.guest = None     # Гость, сидящий за столом (по умолчанию None)

# Класс Guest представляет гостя, наследуется от threading.Thread
class Guest(threading.Thread):
    def __init__(self, name):
        super().__init__()   # Инициализация родительского класса Thread
        self.name = name     # Имя гостя

    def run(self):
        # Гость ждет случайное время от 3 до 10 секунд
        time.sleep(random.uniform(3, 10))

# Класс Cafe управляет столов и гостями, использует очередь для гостей
class Cafe:
    def __init__(self, *tables):
        self.tables = list(tables)  # Список столов в кафе
        self.queue = Queue()        # Очередь для гостей

    def guest_arrival(self, *guests):
        for guest in guests:
            # Ищем свободный стол
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest  # Садим гостя за стол
                    guest.start()        # Запускаем поток гостя
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    break
            else:
                # Все столы заняты, гость в очереди
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None:
                    if not table.guest.is_alive():
                        # Гость закончил прием пищи
                        print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {table.number} свободен")
                        # Освобождаем стол
                        previous_guest = table.guest
                        table.guest = None
                        # Если есть гости в очереди и стол освободился
                        if not self.queue.empty():
                            next_guest = self.queue.get_nowait()
                            next_guest.start()  # Запускаем поток следующего гостя
                            table.guest = next_guest
                            print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
            # Задержка для избежания зацикливания
            time.sleep(1)

# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Создание объекта кафе с заданными столами
cafe = Cafe(*tables)

# Прием гостей в кафе
cafe.guest_arrival(*guests)

# Обслуживание гостей в кафе
cafe.discuss_guests()