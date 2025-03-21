"""
Пример работы с функцией copy

lst1 = [1, 2, 3, 4, 5]

lst3 = lst1.copy()

lst3[2] = 100

print(lst1)
print(lst3)
"""

#nums = list(map(int, input().split()))
"""
input().split() - разделяет строку на части по пробелам.
map(функция, список) - применяет функцию к каждому элементу списка.
list() - преобразует объект map в список. 
"""

nums = [1, 2, 3, 4, 5, 6]
n = 2
lst = nums[-1::] + nums[:-1:]
print(lst)
