s = input()
separator = 0
result = 0
digit = '1234567890'

for value in s:
    if value in digit:
        separator = separator * 10 + int(value)
    else:
        result += separator
        separator = 0
result += separator
print(result)