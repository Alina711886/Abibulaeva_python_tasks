# Dict12. Построить словарь из N пар с различными значениями. 
# Построить обращённый словарь: значение → ключ. 
# Вывести его пары в порядке добавления исходного.

n = int(input())
d = {}
pairs = []

for i in range(n):
    key = input()
    value = input()
    d[key] = value
    pairs.append((key, value))

rev = {}
for key, value in pairs:
    rev[value] = key

for value, key in rev.items():
    print(value, key)
