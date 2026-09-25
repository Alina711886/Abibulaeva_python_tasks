# Begin24. Даны переменные A, B, C. Изменить их значения, переместив содержимое A в C,
# C — в B, B — в A, и вывести новые значения переменных A, B, C.

A = float(input())
B = float(input())
C = float(input())

A, B, C = B, C, A

print(A)
print(B)
print(C)