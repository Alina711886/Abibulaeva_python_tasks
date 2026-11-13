# Proc3. Описать функцию mean(x, y), возвращающую среднее арифметическое и среднее геометрическое (корень из произведения) двух положительных чисел.
# Найти оба средних для пар (A, B), (A, C), (A, D), если даны A, B, C, D.

def mean(x, y):
    amean = (x + y) / 2
    gmean = (x * y) ** 0.5
    return amean, gmean

a = float(input())
b = float(input())
c = float(input())
d = float(input())

am, gm = mean(a, b)
print(am)
print(gm)

am, gm = mean(a, c)
print(am)
print(gm)

am, gm = mean(a, d)
print(am)
print(gm)