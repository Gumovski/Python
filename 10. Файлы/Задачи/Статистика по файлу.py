letters = 0
words = 0
lines = 0
allowed = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
with open('Inp.txt') as f:
    for line in f:
        w = line.split()
        words += len(w)
        for l in line:
            if l in allowed:
                letters += 1
        lines += 1
print(f'Input file contains\n{letters} letters \n{words} words \n{lines} lines')

