import threading
import random
import time
from threading import Lock


class Bank:
    def __init__(self):
        self.balance = 0
        self.takeLock = Lock()
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            with self.lock:
                amount = random.randint(50, 500)
                self.balance += amount
                print(f'Пополнение #{i}: {amount}. Баланс: {self.balance}')
                if self.balance >= 500 and self.takeLock.locked():
                    self.takeLock.release()
            time.sleep(0.001)

    def take(self):
         for i in range(100):
             with self.lock:
                 if not self.takeLock.locked():
                    amount = random.randint(50, 500)
                    print(f'Запрос #{i} на {amount}')
                    if amount <= self.balance:
                        self.balance -= amount
                        print(f'Снятие: {amount}. Баланс: {self.balance}')
                    else:
                        print('Запрос отклонён, недостаточно средств')
                        self.takeLock.acquire(blocking=True)
             time.sleep(0.001)

# Создаем экземпляр банка
bk = Bank()

# Создаем потоки
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

# Запускаем потоки
th1.start()
th2.start()

# Ожидаем завершения потоков
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')