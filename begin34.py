# Begin34. Известно, что X кг шоколадных конфет стоит A рублей, а Y кг ирисок стоит B рублей.
# Определить, сколько стоит 1 кг шоколадных конфет, 1 кг ирисок, а также во сколько раз шоколадные конфеты дороже ирисок.

X = float(input())
A = float(input())

Y = float(input())
B = float(input())

priceX = A / X
priceY = B / Y

difference = priceX / priceY

print(priceX)
print(priceY)
print(difference)