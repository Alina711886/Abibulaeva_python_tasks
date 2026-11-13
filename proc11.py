# Proc11. Функция minmax(x, y) возвращает пару (меньшее, большее).
# Четырьмя вызовами найти минимум и максимум четырёх данных чисел A, B, C, D

def minmax(x, y):
    return min(x, y), max(x, y)

a = float(input())
b = float(input())
c = float(input())
d = float(input())

a, b = minmax(a, b)
c, d = minmax(c, d)
a, c = minmax(a, c)
b, d = minmax(b, d)

print(a)
print(d)