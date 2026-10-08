# List10. Дан список из N строк.
# Вывести самую длинную и самую короткую строку (первую из встретившихся) и их длины.

n = int(input())
a = []

for i in range(n):
    a.append(input())

maxi = a[0]
mini = a[0]

for x in a:
    if len(x) > len(maxi):
        maxi = x
    if len(x) < len(mini):
        mini = x

print(maxi, len(maxi))
print(mini, len(mini))