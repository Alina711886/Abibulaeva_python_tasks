# Boolean10. Проверить истинность высказывания:
# «Ровно одно из чисел A и B нечетное».

a = int(input())
b = int(input())

print(a % 2 != 0 and b % 2 == 0 or a % 2 == 0 and b % 2 != 0)