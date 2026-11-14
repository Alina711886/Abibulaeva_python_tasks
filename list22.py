# List22. Дан список A из N чисел и число D.
# Генератором вывести элементы, умноженные на D, и количество элементов, равных D

n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

d = int(input())
num = [d * x for x in a]

print(num)
print(a.count(d))