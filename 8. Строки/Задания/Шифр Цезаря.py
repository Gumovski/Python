def encode(text,offset):
    up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    l ='abcdefghijklmnopqrstuvwxyz'
    result = ''
    index = 0

    for letter in text:
        if letter in up:
            index = (up.index(letter) + offset) % len(up)
            result += up[index]
        elif letter in l:
            index = (l.index(letter) + offset) % len(l)
            result += l[index]
        else:
            result += letter
    return result

def decode(text,offset):
    return encode(text,-offset)

cezar = decode('CdEza', 2)
print(cezar)