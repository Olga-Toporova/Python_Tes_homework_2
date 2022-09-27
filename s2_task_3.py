'''
Задание 3.
Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
Пример:
Для n = 5: сумма = 11,55
'''

n = int(input("Введите число: "))
num_list = list()
result = 0
for i in range(1, n+1):
    formule = (1 + 1/i)**i
    num_list.append(round(formule, 2))
    result += formule
result = round(result, 2)
print(f" {num_list} -> {result}")