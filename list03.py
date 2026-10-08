# List3. Дан список A из N.
# Вывести сумму элементов и произведение элементов с чётными индексами (0, 2, 4...)

n = int(input())
a = []

summa = 0
product = 1

for i in range(n):
    a.append(int(input()))
    
    if i % 2 == 0:
        summa += a[i]
        product *= a[i]

print(summa)
print(product)