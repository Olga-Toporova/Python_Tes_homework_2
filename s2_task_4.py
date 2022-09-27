'''
Задание 4.
Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt 
в одной строке одно число.
'''

N = int(input("Введите количество элементов: "))
with open('file_for_task_4.txt') as file:
    position_one = int(file.readline())
    position_two = int(file.readline())
result = 1
numbers_list = list()
for n in range(-N, N+1):
    numbers_list.append(n)
    if n == position_one or n == position_two:
        result *= numbers_list[n-1]

print(f"{numbers_list} -> {result}")