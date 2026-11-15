# File1. Дана строка S. Если S — допустимое имя файла, создать пустой файл с этим именем и вывести True, иначе False.

import os

s = input()

if '/' in s or '\\' in s:
    print(False)
else:
    try:
        with open(s, 'x'):
            pass
        print(True)
    except (FileExistsError, OSError):
        print(False)