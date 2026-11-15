# File9. Даны имена двух файлов: один существует и непуст (не обязательно первый), другой отсутствует. 
# Создать отсутствующий и записать в него конечный и начальный элементы существующего.

import os

name1 = input()
name2 = input()

if os.path.isfile(name1) and not os.path.isfile(name2):
    existing, missing = name1, name2
elif os.path.isfile(name2) and not os.path.isfile(name1):
    existing, missing = name2, name1
else:
    exit()

with open(existing, 'r', encoding='utf-8') as f:
    lines = f.readlines()

first_elem = lines[0].rstrip('\n')
last_elem = lines[-1].rstrip('\n')

with open(missing, 'w', encoding='utf-8') as f:
    f.write(last_elem + '\n')
    f.write(first_elem + '\n')