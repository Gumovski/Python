lst = [5, 76, 21, 36, 11, 74, 944, 254]
# 11 21 74 254 944 5 36 76

# Сортируем по последней цифре, а если цифры одинаковые, то сортируется по значению всего числа
lst.sort(key=lambda x: (x % 10, x))
print(lst)

strings = ['zf', 'ab', 'bca', 'b', 'kl', 'dft', 'ez', 'a']
strings.sort(key=lambda s: (len(s), s))
print(strings)
