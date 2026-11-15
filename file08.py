# File8. Даны имена двух файлов: первый существует и непуст, второй отсутствует. 
# Создать второй и записать в него первый и последний элементы первого.

file1 = input()
file2 = input()

with open(file1, 'r') as f:
    lines = f.readlines()

first_elem = lines[0].rstrip('\n')
last_elem = lines[-1].rstrip('\n')

with open(file2, 'w') as f:
    f.write(first_elem + '\n')
    f.write(last_elem + '\n')