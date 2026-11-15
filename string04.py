# String4. Дано N (1 ≤ N ≤ 26). Вывести строку из N первых заглавных латинских букв.

n = int(input())
result = ''

for i in range(n):
    result += chr(ord('A') + i)
    
print(result)