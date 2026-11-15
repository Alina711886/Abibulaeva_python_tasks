# Dict15. Построить словари из N и M пар. Добавить в первый пары второго без update: 
# только ключи, которых нет; совпавшие ключи считать проигнорированными. 
# Вывести размер и число проигнорированных.

n = int(input())
d1 = {}
for i in range(n):
    key = input()
    value = input()
    d1[key] = value

m = int(input())
d2 = {}
for i in range(m):
    key = input()
    value = input()
    d2[key] = value

ignor = 0
for key in d2:
    if key in d1:
        ignor += 1
    else:
        d1[key] = d2[key]

print(len(d1))
print(ignor)