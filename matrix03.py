# Matrix3. Даны M, N и набор из M чисел.
# Сформировать матрицу, у которой в каждом столбце содержатся все числа набора в том же порядке.

m = int(input())
n = int(input())

a = []
for i in range(m):
    a.append(int(input()))

b = []
for i in range(n):
    b.append(a[:])

final_b = [[a[i] for i in range(n)] for i in range(m)]

for row in final_b:
    print(row)
