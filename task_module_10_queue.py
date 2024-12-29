from queue import Queue
from time import sleep
from threading import Thread
from random import randint


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.table = None
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:
            self.table = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f'{guest.name} сел(а) за стол {table.number}')
                    self.table = True
                    break
            if not self.table:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while not self.queue.empty() or self.checking_tables() is True:
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушел(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                if not self.queue.empty() and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()

    def checking_tables(self):
        for table in self.tables:
            if table.guest is not None:
                return True
            else:
                return False


tables = [Table(number) for number in range(1, 6)]
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Daria', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()

# Консоль

# Maria сел(а) за стол 1
# Oleg сел(а) за стол 2
# Vakhtang сел(а) за стол 3
# Sergey сел(а) за стол 4
# Daria сел(а) за стол 5
# Arman в очереди
# Vitoria в очереди
# Nikita в очереди
# Galina в очереди
# Pavel в очереди
# Ilya в очереди
# Alexandra в очереди
# Sergey покушал(-а) и ушел(ушла)
# Стол номер 4 свободен
# Arman вышел(-ла) из очереди и сел(-а) за стол номер 4
# ...
# Alexandra покушал(-а) и ушел(ушла)
# Стол номер 5 свободен
# Ilya покушал(-а) и ушел(ушла)
# Стол номер 1 свободен