def shift_right(s, count):
    return s[-count::] + s[:-count]


def shift_left(s, count):
    return s[count::] + s[:count]

count = int(input())
s = list(map(int, input().split()))
print(shift_right(s, count))
print(shift_left(s, count))
# 6 5 4 3 2
# 2
 # 4 3 2 6 5
