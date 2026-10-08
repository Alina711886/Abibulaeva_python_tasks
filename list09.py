# List9. Дан список A из N чисел.
# Вывести элементы, большие среднего арифметического всех элементов, и их количество.

n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

summa = 0
for i in a:
    summa += i

arithmetic_mean = summa / len(a)

b = []
for x in a:
    if x > arithmetic_mean:
        b.append(x)

print(b)
print(len(b))