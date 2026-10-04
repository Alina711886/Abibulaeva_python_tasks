# For11. Дано N (> 0). Найти сумму N2 + (N + 1)2 + (N + 2)2 + ... + (2·N)2.

n = int(input())

total = 0

for i in range(n + 1):
    total += (n + i) ** 2

print(total)