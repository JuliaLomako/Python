#print(f"Второе число {second} квадрат первого числа {first}")
#elif first * first != second:
#else:
#    print(f"Второе число {second} не является квадратом друг друга") 

#Задача 2 Напишите программу, которая на вход принимает 5 чисел и 
#находит максимальное из них.

# Примеры:
# 1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90


# max_num = int(input("Введите число: "))
# for i in range(4):
#     next_num = int(input("Введите новое число: "))
#     if max_num < next_num:
#         max_num = next_num
# print("Максимальное число среди введенных ", max_num)


# Напишите программу, которая будет на вход принимать число N и выводить 
# числа от -N до N
# Примеры:
# 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5



# N = int(input("Введите число: "))
# for i in range(-N, N+1):
#     print(i, end=" ")
# print()

# Напишите программу, которая будет принимать на вход дробь и показывать 
# первую цифру дробной части числа.
# Примеры:
# 6,78 -> 7
# 5 -> нет
# 0,34 -> 3


# x = float(input("Ваше дробное число: "))
# x = int( (x*10) % 10 )
# print(x)


# Напишите программу, которая проверит истинность утверждения ¬(X ⋁ Y) = ¬X ⋀ ¬Y

# def julia (x):
#     if x == 10:
#         return "в десяточку"
#     elif x == 2.5:
#         return  "лови 25" 
#     elif x == 16:
#         return "еху"

# num = 16
# print(julia(num))



