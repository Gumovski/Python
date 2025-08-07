n = int(input())
d = {}

for i in range(n):
    word = input()
    string = word.split(' - ')
    english = string[0]
    latin = string[1]