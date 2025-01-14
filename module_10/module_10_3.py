# Импорт необходимых библиотек для многопоточности, генерации случайных чисел и работы с задержками
import threading
import random
import time
from threading import Lock


class Bank:
    def __init__(self):
        # Инициализация начального баланса
        self.balance = 0

        # Блокировка для управления доступом к снятию средств
        # Используется для синхронизации потоков при недостатке средств
        self.takeLock = Lock()

        # Основной замок для потокобезопасного доступа к балансу
        self.lock = Lock()

    def deposit(self):
        # Метод для пополнения баланса
        for i in range(100):
            # Использование блокировки для потокобезопасного доступа к балансу
            with self.lock:
                # Генерация случайной суммы пополнения
                amount = random.randint(50, 500)

                # Увеличение баланса
                self.balance += amount

                # Вывод информации о пополнении
                print(f'Пополнение #{i}: {amount}. Баланс: {self.balance}')

                # Если баланс достаточен и takeLock заблокирован, освободить его
                if self.balance >= 500 and self.takeLock.locked():
                    self.takeLock.release()

            # Небольшая задержка для имитации реалистичности операций
            time.sleep(0.001)

    def take(self):
        # Метод для снятия средств
        for i in range(100):
            # Использование блокировки для потокобезопасного доступа к балансу
            with self.lock:
                # Проверка, что блокировка снятия не активна
                if not self.takeLock.locked():
                    # Генерация случайной суммы снятия
                    amount = random.randint(50, 500)

                    # Вывод информации о запросе на снятие
                    print(f'Запрос #{i} на {amount}')

                    # Проверка достаточности средств
                    if amount <= self.balance:
                        # Уменьшение баланса
                        self.balance -= amount
                        print(f'Снятие: {amount}. Баланс: {self.balance}')
                    else:
                        # Если средств недостаточно, блокируем возможность снятия
                        print('Запрос отклонён, недостаточно средств')
                        self.takeLock.acquire(blocking=True)

            # Небольшая задержка для имитации реалистичности операций
            time.sleep(0.001)


# Создаем экземпляр банка
bk = Bank()

# Создаем потоки для пополнения и снятия
# Используем метод класса с передачей экземпляра в качестве аргумента
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

# Запускаем потоки
th1.start()
th2.start()

# Ожидаем завершения обоих потоков
th1.join()
th2.join()

# Вывод итогового баланса
print(f'Итоговый баланс: {bk.balance}')