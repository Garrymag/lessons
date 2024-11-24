def test_function():
    # Определяем внутреннюю функцию inner_function
    def inner_function():
        # Эта функция печатает сообщение
        print("Я в области видимости функции test_function")

    # Вызываем inner_function внутри test_function
    inner_function()


# Вызываем test_function, чтобы увидеть результат
test_function()

# Попробуем вызвать inner_function вне test_function
inner_function()
