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
left_part = ''
for i in range(len(alphabet) - 1, -1, -1):
    count = sort.count(alphabet[i])
    left_part += alphabet[i] * (count // 2)
#
right_part = left_part[::-1]
result = left_part
if len(sort) % 2 == 1:
    result += odd_letter
result += right_part
#
print(result.upper())
