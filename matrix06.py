# Matrix6. Даны M, N, число Q и набор из N чисел. Первая строка — набор; каждая следующая строка равна предыдущей, умноженной на Q по столбцам.

m = int(input())
n = int(input())
q = int(input())

a = []
for i in range(n):
    a.append(int(input()))

b = []
row = a[:]
for i in range(m):
    b.append(row[:])
    row = [row[j] * q for j in range(n)]

for i in range(m):
    print(b[i])
