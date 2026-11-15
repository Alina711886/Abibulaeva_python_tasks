# Dict7. Построить словарь из N пар. Вывести ключ с наибольшим значением 
# (перебор с кандидатом; значения различны).

n = int(input())
d = {}

for i in range(n):
    key = input()
    value = int(input())
    d[key] = value

max_key = 0
max_value = 0

for key, value in d.items():
    if value > max_value:
        max_value = value
        max_key = key

print(max_key)
