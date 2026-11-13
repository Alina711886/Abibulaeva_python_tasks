# Proc7. Функция invert_digits(k) возвращает число с обратным порядком цифр.
# Перевернуть пять данных чисел

def invert_digits(k):
    reverse_k = ''

    while k > 0:
        reverse_k += str(k % 10)
        k //= 10
    return int(reverse_k)

for i in range(5):
    k = int(input())
    print(invert_digits(k))