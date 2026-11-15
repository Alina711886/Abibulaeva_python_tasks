# Class4. Класс Potion: name, price, heal в __init__; метод describe() возвращает строку «name: price gold, +heal health»; вывести результат метода.

class Potion:
    def __init__(self, name, price, heal):
        self.name = name
        self.price = price
        self.heal = heal

    def describe(self):
        return f"{self.name}: {self.price} gold, +{self.heal} health"

name = input()
price = int(input())
heal = int(input())

p = Potion(name, price, heal)
print(p.describe())