# While2. Даны положительные A и B (A > B). Не используя * и /,
# найти количество отрезков B, размещенных на отрезке A.

a = int(input())
b = int(input())

free = a
count = 0

while free >= b:
    free -= b
    count += 1

print(count)