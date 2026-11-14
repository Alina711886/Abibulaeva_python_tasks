# List25. Дан список A из N различных чисел.
# Вывести второй по величине элемент

n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

print(sorted(a, reverse=True)[1])