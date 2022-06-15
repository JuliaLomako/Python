# Задача 1: Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_odd_number(list):
    for i in list:
        sum_num = sum(list[1::2])
        return sum_num        
my_list = [2, 3, 5, 9, 3]
print("сумма эллементов на нечётной позиции равна: " , sum_odd_number(my_list))


# Задача 2:Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. 
# Если остается 1 элемент без пары - умножаем его самого на себя.

# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


def product_pairs_numbers(list):
    product = []
    for i in range((len(list)+1)//2):
        product.append(list[i]*list[len(list)-1-i])
    return product

init_list = [2, 3, 4, 5, 6]
print(init_list, end=' => ')
print(product_pairs_numbers(init_list))

# Задача 3: Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
#  максимальным и минимальным значением дробной части элементов.

# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def difference_max_min(lst):
    result = []
    for index in range(len(lst)):
        result.append(round(lst[index]%1, 2))

    return max(result) - min(result)

my_list = [1.1, 1.2, 3.1, 5, 10.01]
print(f'{my_list} => {difference_max_min(my_list)}')
