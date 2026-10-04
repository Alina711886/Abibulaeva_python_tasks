# While9. Дано N (> 0). Найти наибольшее K, для которого K*K <= N.

n = int(input())

k = 0

while 3 ** k <= n:
    k += 1

print(k)