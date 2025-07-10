word = input()
result = []
count = 0
for letter in word:
    if letter == 'a':
        result.append('b')
        count += 1
    elif letter == 'A':
        result.append('B')
        count += 1
    elif letter == 'b':
        result.append('a')
        count += 1
    elif letter == 'B':
        result.append('A')
        count += 1
    else:
        result.append(letter)

print(f'Итог:{"".join(result)} \n Кол.изменений:{count}')
