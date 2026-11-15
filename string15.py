# String15. Дана строка. Подсчитать общее количество строчных латинских и русских букв в ней.

s = input()
count = 0

for ch in s:
    if ('a' <= ch <= 'z') or ('а' <= ch <= 'я') or ch == 'ё':
        count += 1
        
print(count)