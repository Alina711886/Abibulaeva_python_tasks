# List7. Дан список A из N чисел.
# Вывести элементы в обратном порядке, не меняя исходный список; затем вывести исходный.

n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

b = a[::-1]

print(b)
print(a)