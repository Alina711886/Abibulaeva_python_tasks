# If5. Найти количество положительных и количество отрицательных чисел в исходном наборе.

a = int(input())
b = int(input())
c = int(input())

count_p = (a > 0) + (b > 0) + (c > 0)
count_o = (a < 0) + (b < 0) + (c < 0)

print(count_p)
print(count_o)