# List15. Дан список A из N чисел.
# Вывести элементы на нечётных позициях (1, 3, 5... при счёте позиций с 1) и их сумму

n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

d = a[::2]

summa = 0
for x in d:
    summa += x

print(d)
print(summa)