# Proc20. Функция triangle_p(a, h) возвращает периметр равнобедренного треугольника 
# по основанию a и высоте h к основанию; боковая сторона b^2 = (a/2)^2 + h^2. 
# Найти периметры трёх треугольников.

def triangle_p(a, h):
    half_base = a / 2
    side = (half_base ** 2 + h ** 2) ** 0.5
    return a + 2 * side

for i in range(3):
    a = float(input())
    h = float(input())
    print(triangle_p(a, h))