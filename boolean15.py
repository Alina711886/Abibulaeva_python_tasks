# Boolean15. Проверить истинность высказывания:
# «Ровно два из чисел A, B, C являются положительными».

a = int(input())
b = int(input())
c = int(input())

count = (a > 0) + (b > 0) + (c > 0)

print(count == 2)