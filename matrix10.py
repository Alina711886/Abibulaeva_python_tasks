# Matrix10. Дана матрица M × N. Вывести элементы столбцов с нечётными номерами (1, 3, ...) по столбцам, без условного оператора.

m = int(input())
n = int(input())

a = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(int(input()))
    a.append(row)

for j in range(0, n, 2):
    for i in range(m):
        print(a[i][j])
