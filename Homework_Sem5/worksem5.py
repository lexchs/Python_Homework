# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# def exponentiation(a,b):
#     if b == 0:
#         return 1
#     return a * exponentiation(a,b-1)
    
# a = int(input("Enter number: "))
# b = int(input("Enter exponent: "))
# print(exponentiation(a,b))


# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# *Пример:*
# 2 2
# 4


# def sum(a,b):
#     if b == 0:
#         return a
#     return sum(a+1,b-1)

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# print(sum(a,b))


# Случайно получилось сделать функцию умножения без умножения)
# def sum(a,b):
#     if b == 0:
#         return 0
#     return a + sum(a,b-1)