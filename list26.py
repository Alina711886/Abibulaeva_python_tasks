# List26. Дан список A из N чисел.
# Генератором вывести элементы, большие среднего, и само среднее

n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

average_value = sum(a) / len(a)

above_average = [x for x in a if x > average_value]

print(above_average)
print(average_value)