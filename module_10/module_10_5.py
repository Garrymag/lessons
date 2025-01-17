import threading
import time
import random
from queue import Queue


class Table:
    """
    Класс Table представляет стол в кафе.

    Атрибуты:
        number (int): Номер стола.
        guest (Guest or None): Гость, сидящий за столом. Изначально None.
    """

    def __init__(self, number):
        """
        Инициализирует стол с заданным номером.

        :param number: Номер стола.
        """
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    """
    Класс Guest представляет гостя, который является потоком.

    Наследуется от threading.Thread.

    Атрибуты:
        name (str): Имя гостя.
    """

    def __init__(self, name):
        """
        Инициализирует гостя с заданным именем.

        :param name: Имя гостя.
        """
        super().__init__()
        self.name = name

    def run(self):
        """
        Метод, выполняемый при запуске потока.
        Гость "ест" в течение случайного времени от 3 до 10 секунд.
        """
        # Генерируем случайное время ожидания от 3 до 10 секунд
        wait_time = random.randint(3, 10)
        time.sleep(wait_time)


class Cafe:
    """
    Класс Cafe представляет кафе с определенным количеством столов и управляет гостями.

    Атрибуты:
        queue (Queue): Очередь гостей, ожидающих посадки.
        tables (list of Table): Список столов в кафе.
    """

    def __init__(self, *tables):
        """
        Инициализирует кафе с заданными столами.

        :param tables: Произвольное количество объектов класса Table.
        """
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        """
        Обрабатывает прибытие гостей: пытается посадить их за свободные столы или помещает в очередь.

        :param guests: Произвольное количество объектов класса Guest.
        """
        for guest in guests:
            # Ищем первый свободный стол
            free_table = None
            for table in self.tables:
                if table.guest is None:
                    free_table = table
                    break
            if free_table:
                # Посадим гостя за найденный свободный стол
                free_table.guest = guest
                guest.start()  # Запускаем поток гостя
                print(f"{guest.name} сел(-а) за стол номер {free_table.number}")
            else:
                # Помещаем гостя в очередь
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        """
        Имитирует процесс обслуживания гостей: освобождает столы по окончании приема пищи и
        садит новых гостей из очереди.

        Обслуживание продолжается, пока есть гости в очереди или занятые столы.
        """
        # Цикл, который продолжается, пока есть гости в очереди или занятые столы
        while not self.queue.empty() or self.has_occupied_tables():
            # Проходим по всем столам в кафе
            for table in self.tables:
                # Проверяем, занят ли текущий стол
                if table.guest is not None:
                    guest = table.guest  # Получаем текущего гостя за столом
                    # Проверяем, жив ли гость (т.е. закончил ли он прием пищи)
                    if not guest.is_alive():
                        # Гость закончил прием пищи и покидает кафе
                        print(f"{guest.name} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {table.number} свободен")
                        table.guest = None  # Освобождаем стол

                        # Если в очереди есть гости, садим следующего за освобожденный стол
                        if not self.queue.empty():
                            next_guest = self.queue.get()  # Получаем следующего гостя из очереди
                            table.guest = next_guest  # Сажаем нового гостя за стол
                            next_guest.start()  # Запускаем процесс для нового гостя
                            print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")

            # Добавляем небольшую задержку, чтобы избежать перегрузки процессора
            time.sleep(1)

    def has_occupied_tables(self):
        """
        Проверяет, есть ли занятые столы в кафе.

        Возвращает True, если хотя бы один стол занят, иначе False.
        """
        for table in self.tables:
            if table.guest is not None:  # Если стол занят
                return True  # Возвращаем True, если нашли занятой стол
        return False  # Если ни один стол не занят, возвращаем False


# Создание столов
tables = [Table(number) for number in range(1, 6)]

# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

# Создание гостей
guests = [Guest(name) for name in guests_names]

# Заполнение кафе столами
cafe = Cafe(*tables)

# Приём гостей
cafe.guest_arrival(*guests)

# Обслуживание гостей
cafe.discuss_guests()