# Proc8. Функция add_right_digit(d, k) возвращает число k с приписанной справа цифрой d (0–9).
# Приписать к данному K справа D1 и D2, печатая результат каждого шага

def add_right_digit(d, k):
    return k * 10 + d

d1 = int(input())
k = int(input())
result_1 = add_right_digit(d1, k)
print(result_1)

d2 = int(input())
result_2 = add_right_digit(d2, result_1)
print(result_2)