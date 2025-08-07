d = {}
text = input()
for letter in text:
    if letter in d:
        d[letter] += 1
    else:
        d[letter] = 1
for key,value in d.items():
    print(f'{key} - {value}')