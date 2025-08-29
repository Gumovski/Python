a = list(map(int, input().split()))
mini = 0
maxi = 0
for i in range(len(a)):
    if a[mini] < a[i]:
         mini = i
    if a[maxi] > a[i]:
        maxi = i
a[mini], a[maxi] = a[maxi], a[mini]
print(*a)