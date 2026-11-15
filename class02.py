# Class2. К классу Point добавить метод shift(dx, dy), меняющий координаты; применить и вывести поля.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def shift(self, dx, dy):
        self.x += dx
        self.y += dy

x = int(input())
y = int(input())
dx = int(input())
dy = int(input())

p = Point(x, y)
p.shift(dx, dy)

print(p.x)
print(p.y)