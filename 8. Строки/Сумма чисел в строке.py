s = input()
num = 0
result = 0

for value in s:
    if value.isdigit():
        separator = num * 10 + int(value)
    else:
        result += num
        num = 0
result += num
print(result)