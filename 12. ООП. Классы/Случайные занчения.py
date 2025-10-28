"""
random.randint(a, b) - случайное целое число от a до b включительно
random.random() - случайное дробное число от 0 до 1 не включая 1
random.uniform(a, b) - случайное дробное число от a до b включительно
random.choice(sequence) - случайный элемент последовательности sequence
random.randrange([start], stop[, step]) - случайное число в диапазоне [start, stop) с шагом step
random.shuffle(x[, random]) - перемешивает последовательность x на месте
random.sample(population, k) - список из k элементов population без повторений
"""
import random

print(random.randint(1, 9))
print(random.randrange(1, 10))
print(random.random())
print(random.uniform(1, 9))
