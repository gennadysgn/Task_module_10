import threading
from random import randint
from time import sleep


class Bank:

    def __init__(self):
        self.balance = int(0)
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            dep = randint(50, 500)
            self.balance += dep
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {dep}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            t = randint(50, 500)
            print(f'Запрос на {t}')
            if t <= self.balance:
                self.balance -= t
                print(f'Снятие: {t}. Баланс: {self.balance}')
            elif t > self.balance:
                print('Запрос отклонен, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

# Консоль

# Пополнение: 352. Баланс: 352
# Запрос на 442
# Запрос отклонен, недостаточно средств
# Пополнение: 446. Баланс: 798
# Запрос на 442
# Снятие: 442. Баланс: 356
# Пополнение: 414. Баланс: 770
# Запрос на 478
# Снятие: 478. Баланс: 292
# Пополнение: 258. Баланс: 550
# Запрос на 91
# Снятие: 91. Баланс: 459
# Пополнение: 494. Баланс: 953
# Запрос на 430
# Снятие: 430. Баланс: 523
# Пополнение: 114. Баланс: 637Запрос на 290
# Снятие: 290. Баланс: 347

# ....
# Запрос на 164
# Снятие: 164. Баланс: 269
# Пополнение: 135. Баланс: 404
# Запрос на 435
# Запрос отклонен, недостаточно средств
# Пополнение: 96. Баланс: 500
# Итоговый баланс: 500
