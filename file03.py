# File3. Дано имя файла и вещественные A и D. Записать в файл 10 первых членов прогрессии A, A+D, A+2·D, ...

name = input()
a = float(input())
d = float(input())

with open(name, 'w') as f:
    for i in range(10):
        value = a + i * d
        f.write(str(value) + '\n')