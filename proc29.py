# Proc29. Функция digit_count(k) возвращает количество цифр k (> 0). 
# Найти количество цифр пяти чисел.

def digit_count(k):
    count = 0
    while k > 0:
        k //= 10
        count += 1
    return count

for i in range(5):
    k = int(input())
    print(digit_count(k))