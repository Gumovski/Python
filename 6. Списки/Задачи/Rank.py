s = [165, 163, 160, 160, 157, 157, 155, 154]
sp = [162]
stepTrue = []
stepFalse = []
main =  []
count = 0
for i in range(len(s)):
    if s[i] >= sp[0]:
        stepTrue.append(s[i])
        count += 1
    else:
        stepFalse.append(s[i])
main.append(stepTrue)
main.append(sp)
main.append(stepFalse)

print(count + 1)