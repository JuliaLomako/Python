# Задача 1(33): Задана натуральная степень k. Сформировать случайным образом список
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


# import random
# k = int(input("Введите степень многочлена: "))

def random_list (k: int):
    s = " "
    file = open('list.txt', 'w')
    while k > 1:
            n = str(random.randint(0, 100))
            s = s + (f'{n}^({str(k)}) + ')
            k -= 1
            if k == 1:
                s += str(random.randint(0, 100))
    file.write(s)

random_list(k)


# Задача 2(35): В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найти его.


from os import system
system("cls")


with open('in.txt', 'r') as data:
    st = data.read()

init_set = set(map(int, st.split()))
print(f'Данные в файле (in.txt): {st}')
help_set = {i for i in range(min(init_set), max(init_set)+1)}
print(f'Недостающее число: {(help_set.difference(init_set)).pop()}')


# Задача 3(43)Дана последовательность чисел. Получить список уникальных элементов
# заданной последовательности.
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# вариант 1

numbers = [1, 2, 3, 5, 1, 5, 3, 10] 

def unique_list(num):
    new_list = []
    for i in num:
        if numbers.count(i) > 1:
            continue
        else:
            new_list.append(i)
    return new_list 
                                                           
print(unique_list(numbers))

# вариант 2 (после повторного просмотра лекции, родилось так ))

numbers = [1, 2, 3, 5, 1, 5, 3, 10] 
new_list = [ i for i in numbers if numbers.count(i) == 1]
print(new_list)

