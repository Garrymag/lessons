import os  # Импортируем модуль os для работы с файловой системой

# Определяем класс Product
class Product:
    def __init__(self, name: str, weight: float, category: str):
        """
        Инициализация нового экземпляра класса Product.

        :param name: Название продукта.
        :param weight: Вес продукта в килограммах.
        :param category: Категория продукта.
        """
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self) -> str:
        """
        Возвращает строковое представление экземпляра Product.

        :return: Строка, описывающая продукт.
        """
        return f"{self.name}, {self.weight}, {self.category}"


# Определяем класс Shop
class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'  # Имя файла для хранения информации о продуктах

    def get_products(self) -> str:
        """
        Считывает всю информацию о продуктах из файла __file_name и возвращает её в виде строки.
        Если файл не существует, возвращает пустую строку.

        :return: Строка, содержащая все продукты из файла или пустая строка, если файл не найден.
        """
        # Проверяем, существует ли файл
        if not os.path.isfile(self.__file_name):
            return ""  # Если файл не существует, возвращаем пустую строку

        # Открываем файл в режиме чтения
        file = open(self.__file_name, 'r')
        content = file.read()  # Читаем всё содержимое файла
        file.close()  # Закрываем файл
        return content  # Возвращаем прочитанное содержимое

    def add(self, *products: Product):
        """
        Добавляет продукты в файл __file_name, если они ещё не присутствуют.
        Если файл не существует, он будет создан.

        :param products: Произвольное количество объектов класса Product.
        """
        # Читаем существующие продукты из файла
        # Извлекая только названия
        existing_products = []
        for line in self.get_products().splitlines():
            if line:  # Проверяем, что строка не пустая
                product_name = line.split(',')[0]  # Получаем первый элемент (название продукта)
                existing_products.append(product_name)
        for product in products:
            # Проверяем, существует ли уже продукт с таким именем в файле
            if product.name in existing_products:
                print(f"Продукт {product.name} уже есть в магазине")  # Уведомляем, если продукт существует
            else:
                file = open(self.__file_name, 'a')  # Открываем файл в режиме добавления
                file.write(f"{product}\n")  # Записываем продукт в файл с новой строки
                file.close()  # Закрываем файл после записи


# Пример использования классов Product и Shop
if __name__ == "__main__":
    s1 = Shop()  # Создаём экземпляр класса Shop

    # Создание продуктов
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # Печатаем строковое представление p2

    # Добавляем продукты в магазин
    s1.add(p1, p2, p3)

    # Печатаем все продукты в магазине
    print(s1.get_products())