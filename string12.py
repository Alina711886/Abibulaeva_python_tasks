# String12. Даны непустая строка S и N (> 0). 
# Вывести строку из символов S, между которыми вставлено по N звёздочек.

s = input()
n = int(input())

stars = '*' * n
result = s[0]

for i in range(1, len(s)):
    result += stars + s[i]

print(result)