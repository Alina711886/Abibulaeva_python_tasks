# Proc9. Функция add_left_digit(d, k) возвращает число k с приписанной слева цифрой d (1–9).
# Приписать к данному K слева D1 и D2, печатая каждый шаг

def add_left_digit(d, k):
    return int(str(d) + str(k))

d1 = int(input())
k = int(input())
result_1 = add_left_digit(d1, k)
print(result_1)

d2 = int(input())
result_2 = add_left_digit(d2, result_1)
print(result_2)