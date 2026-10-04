# For13. Дано N (> 0). Найти значение выражения 1.1 − 1.2 + 1.3 − ... (N слагаемых, знаки чередуются).

n = int(input())

total = 0.0

for i in range(1, n + 1):
    if i % 2 != 0:
        total += 1 + i / 10
    else:
        total -= 1 + i / 10

print(f"{total:.2f}")