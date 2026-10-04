# For9. Даны A и B (A < B). Найти сумму квадратов всех целых чисел от A до B включительно.

a = int(input())
b = int(input())

total = 0

for i in range(a, b + 1):
    total += i ** 2

print(total)