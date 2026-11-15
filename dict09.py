# Dict9. Построить словари из N и M пар. Слить второй в первый через update. 
# Вывести размер результата и значение ключа, который был в обоих словарях (такой ключ гарантированно есть).

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

k = ""
for key in d2:
    if key in d1:
        k = key
        break

d1.update(d2)

print(len(d1))
print(d1[k])