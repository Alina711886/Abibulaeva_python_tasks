# While14. Дано A (> 1). Вывести наибольшее K, при котором
# сумма 1 + 1/2 + ... + 1/K < A, и саму эту сумму.

a = float(input())

total = 0.0
k = 1

while total + 1 / k < a:
    total += 1 / k
    k += 1


print(k - 1)
print(total)