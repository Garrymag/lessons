import time

class User:
    """
    Класс пользователя платформы
    Хранит основную информацию о пользователе
    """

    def __init__(self, nickname, password, age):
        # Nickname пользователя
        self.nickname = nickname

        # Хэширование пароля для безопасного хранения
        self.password = hash(password)

        # Возраст пользователя
        self.age = age

    def __str__(self):
        # Строковое представление пользователя - его nickname
        return self.nickname


class Video:
    """
    Класс видео на платформе
    Содержит информацию о каждом видео
    """

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        # Заголовок видео
        self.title = title

        # Продолжительность видео в секундах
        self.duration = duration

        # Текущая позиция просмотра
        self.time_now = time_now

        # Возрастное ограничение
        self.adult_mode = adult_mode

    def __eq__(self, other):
        # Метод сравнения видео по названию
        return self.title == other.title


class UrTube:
    """
    Основной класс платформы для управления
    пользователями и видео
    """

    def __init__(self):
        # Список зарегистрированных пользователей
        self.users = []

        # Список доступных видео
        self.videos = []

        # Текущий авторизованный пользователь
        self.current_user = None

    def log_in(self, nickname, password):
        """
        Авторизация пользователя
        """
        # Хэшируем введенный пароль
        hashed_password = hash(password)

        # Поиск пользователя с совпадающими данными
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                return

    def register(self, nickname, password, age):
        """
        Регистрация нового пользователя
        """
        # Проверка существования пользователя
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return

        # Создание нового пользователя
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user

    def log_out(self):
        """
        Выход из аккаунта
        """
        self.current_user = None

    def add(self, *videos):
        """
        Добавление новых видео на платформу
        Исключает дубликаты
        """
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, search_word):
        """
        Поиск видео по ключевому слову
        Регистронезависимый поиск
        """
        return [video.title for video in self.videos
                if search_word.lower() in video.title.lower()]

    def watch_video(self, title):
        """
        Воспроизведение видео с проверками
        """
        # Проверка авторизации
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        # Поиск видео
        for video in self.videos:
            if video.title == title:
                # Проверка возрастного ограничения
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                # Имитация воспроизведения
                for i in range(1, video.duration + 1):
                    print(i, end=' ')
                    time.sleep(0.5)  # Уменьшил время для быстрой проверки

                print("\nКонец видео")
                return


# Блок для полной проверки функционала
def test_urtube():
    print("🔍 Тестирование платформы UrTube")

    # Создание платформы
    ur = UrTube()

    # Создание тестовых видео
    v1 = Video('Лучший язык программирования 2024 года', 10)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print("\n🔎 Тест поиска видео:")
    print("Поиск 'лучший':", ur.get_videos('лучший'))
    print("Поиск 'ПРОГ':", ur.get_videos('ПРОГ'))

    # Проверка просмотра без авторизации
    print("\n🚫 Тест просмотра без авторизации:")
    ur.watch_video('Для чего девушкам парень программист?')

    # Регистрация несовершеннолетнего
    print("\n👦 Регистрация несовершеннолетнего:")
    ur.register('vasya_pupkin', 'password123', 13)
    ur.watch_video('Для чего девушкам парень программист?')

    # Регистрация совершеннолетнего
    print("\n👨 Регистрация совершеннолетнего:")
    ur.register('urban_pythonist', 'password456', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка повторной регистрации
    print("\n🆔 Проверка повторной регистрации:")
    ur.register('vasya_pupkin', 'новый_пароль', 55)

    # Вывод текущего пользователя
    print("\n👤 Текущий пользователь:", ur.current_user)


# Запуск тестирования
test_urtube()