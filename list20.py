# List20. Дан список A из N чисел.
# Генератором построить список квадратов элементов; вывести его и сумму квадратов.

n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

square = [x * x for x in a]

print(square)
print(sum(square))