s = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
sort = ''
#
for letter in s:
    low_letter = letter.lower()
    if low_letter in alphabet:
        sort += low_letter
#
odd = 0
odd_letter = ''
for letter in alphabet:
    count = sort.count(letter)
    if count % 2 != 0:
        odd += 1
        odd_letter = letter
#
if (len(sort) % 2 == 0 and odd != 0) or (len(sort) % 2 != 0 and odd != 1):
    print('NO')
    exit()
#
left_part = []
for i in range(len(alphabet) - 1,-1,-1):
    letter_alphabet = alphabet[i]
    count = 0
    for letter in sort:
        if letter == letter_alphabet:
            count += 1
    for j in range(count // 2):
        left_part.append(letter_alphabet)
#
right_part = left_part[::-1]
result = ''.join(left_part)
if len(sort) % 2 == 1:
    result += odd_letter
result += ''.join(right_part)
#
print(result.upper())