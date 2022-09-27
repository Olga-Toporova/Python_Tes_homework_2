'''
Задание 5.
Реализуйте алгоритм перемешивания списка.(Без использования библиотеки random)
'''
import random
import copy

min = int(input("Введите минимальное значение: "))
max = int(input("Введите максимальное значение: "))

origin_list = list(range(min, max+1))
shuffle_list = copy.copy(origin_list)

list_length = len(shuffle_list)
for i in range(list_length):
    for j in range(list_length - i):
        shuffle_list[i], shuffle_list[j] = shuffle_list[j], shuffle_list[i]

print(origin_list, "-> ", shuffle_list)
