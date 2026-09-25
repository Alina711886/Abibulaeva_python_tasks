# Begin23. Даны переменные A, B, C. Изменить их значения, переместив содержимое A в B,
# B — в C, C — в A, и вывести новые значения переменных A, B, C.

A = float(input())
B = float(input())
C = float(input())

A, B, C = C, A, B

print(A)
print(B)
print(C)