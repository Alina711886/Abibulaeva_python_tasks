# Proc13. Функция sort_dec3(a, b, c) возвращает три значения по убыванию. 
# Упорядочить два набора

def sort_dec3(a, b, c):
    sort_abc = sorted([a, b, c], reverse=True)
    return sort_abc[0], sort_abc[1], sort_abc[2] 

a1 = float(input())
b1 = float(input())
c1 = float(input())

a2 = float(input())
b2 = float(input())
c2 = float(input())

print(sort_dec3(a1, b1, c1))
print(sort_dec3(a2, b2, c2))