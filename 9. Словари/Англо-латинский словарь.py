n = int(input())
d = {}
for i in range(n):
    word = input()
    string = word.split('-')
    english = string[0].strip()
    latin = string[1].split(',')

    for lat in latin:
        lat = lat.strip()
        if lat not in d:
            d[lat] = []
        d[lat].append(english.strip())

latin_s = list(d.keys())
latin_s.sort()

print(len(latin_s))

for lat in latin_s:
    english_s = sorted(d[lat])

    print(f"{lat} - {', '.join(english_s)}")


#3
#apple - malum, pomum, popula
#fruit - baca, bacca, popum
#punishment - malum, multa