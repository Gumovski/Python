mylist = list(map(int, input().split()))
count = 0
for i in range(1,len(mylist) - 1):
    if mylist[i] > mylist[i + 1] and mylist[i] > mylist[i - 1]:
        count += 1
print(count)