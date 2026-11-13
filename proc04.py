# Proc4. Функция triangle_ps(a) возвращает периметр P = 3·a и площадь S = a2·√3/4 равностороннего треугольника.
# Найти P и S трёх данных сторон.

def triangle_ps(a):
    perimeter = 3 * a
    area = a ** 2 * (3 ** 0.5 / 4)
    return perimeter, area

for i in range(3):
    a = float(input())
    print(triangle_ps(a))