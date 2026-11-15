# Dict13. Построить словарь из N троек: название, цена, количество (значение — список из двух чисел).
# Вывести суммарную стоимость склада и название самого дорогого по стоимости предмета.

n = int(input())
d = {}

for i in range(n):
    name = input()
    price = int(input())
    quantity = int(input())
    d[name] = [price, quantity]

cost = 0
expensive_n = None
max_cost = -1

for name, data in d.items():
    price, quantity = data
    item_cost = price * quantity
    cost += item_cost
    if item_cost > max_cost:
        max_cost = item_cost
        expensive_n = name

print(cost)
print(expensive_n)
