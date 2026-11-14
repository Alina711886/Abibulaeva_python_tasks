# List30. Дан список из N строк.
# Генератором вывести список длин строк и суммарную длину всех строк

n = int(input())
a = []

for i in range(n):
    a.append(input())

len_words = [len(x) for x in a]
sum_len_words = sum(len_words)

print(len_words)
print(sum_len_words)