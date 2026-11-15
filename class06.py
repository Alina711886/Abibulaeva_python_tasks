# Class6. Класс Inventory: словарь предметов в __init__; методы add(name, qty) и total() (сумма количеств); вывести total после трёх добавлений.

class Inventory:
    def __init__(self):
        self.items = {}

    def add(self, name, qty):
        if name in self.items:
            self.items[name] += qty
        else:
            self.items[name] = qty

    def total(self):
        return sum(self.items.values())

inv = Inventory()

for i in range(3):
    name = input()
    qty = int(input())
    inv.add(name, qty)

print(inv.total())