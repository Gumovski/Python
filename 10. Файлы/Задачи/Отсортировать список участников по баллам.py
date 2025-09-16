s = []
with open('inpu.txt',encoding='UTF-8') as f:
    for line in f:
        part = line.split()
        surname = part[0]
        name = part[1]
        school = part[2]
        points = int(part[3])
        s.append((surname,name,points))

s.sort(key=lambda x: ( -x[2], x[0], x[1]))

for student in s:
    print(f'{student[0]} {student[1]} {student[2]}')

with open('output.txt','w',encoding='UTF-8') as f:
    for student in s:
        f.write(f'{student[0]} {student[1]} {student[2]}\n')
