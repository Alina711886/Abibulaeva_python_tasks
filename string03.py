# String3. Дан символ C. Вывести символы, предшествующий C в кодовой таблице и следующий за ним.

c = input()
prev_char = chr(ord(c) - 1)
next_char = chr(ord(c) + 1)
print(prev_char, next_char)
