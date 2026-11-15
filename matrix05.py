# Matrix5. Даны M, N, число D и набор из M чисел. Первый столбец — набор; каждый следующий столбец равен предыдущему плюс D по строкам.

m = int(input())
n = int(input())
d = int(input())

a = []
for i in range(m):
    a.append(int(input()))

b = []
for i in range(m):
    row = []
    value = a[i]
    for j in range(n):
        row.append(value)
        value = value + d
    b.append(row)

for i in range(m):
    print(b[i])
