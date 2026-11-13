# Proc18. Функция circle_s(r) возвращает площадь круга радиуса r (π = 3.14). 
# Найти площади трёх кругов.

def circle_s(r):
    pi = 3.14
    return pi * r ** 2

for i in range(3):
    r = float(input())
    print(circle_s(r))
