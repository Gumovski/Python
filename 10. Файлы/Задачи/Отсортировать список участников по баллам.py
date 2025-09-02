s = []
with open('inpu.txt') as f:
    for line in f:
        part = line.split()
        surname = part[0]
        name = part[1]
        school = part[2]
        points = int(part[3])
        s.append((surname,name,points))

for i in range(len(s)):
    for j in range(len(s) - i - 1):
        now = s[j]
        nex = s[j + 1]

        if now[2] < nex[2]:
            s[j], s[j + 1] = s[j + 1], s[j]

        elif now[2] == nex[2]:
            if now[0] > nex[0]:
                s[j], s[j + 1] = s[j + 1], s[j]

            elif now[0] == nex[0]:
                if now[1] > nex[1]:
                    s[j], s[j + 1] = s[j + 1], s[j]

for student in s:
    print(f'{student[0]} {student[1]} {student[2]}')

