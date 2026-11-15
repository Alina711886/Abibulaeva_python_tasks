# Dict14. Построить словарь из N пар и число V. 
# Удалить все пары со значением меньше V, не меняя словарь во время перебора. 
# Вывести размер после удаления.

n = int(input())
d = {}

for i in range(n):
    key = input()
    value = int(input())
    d[key] = value

v = int(input())

remove = []
for key, value in d.items():
    if value < v:
        remove.append(key)

for key in remove:
    del d[key]

print(len(d))
