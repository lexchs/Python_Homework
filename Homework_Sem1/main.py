def sum3digit(x):
    fdx = x//100
    dx = x-(fdx*100)
    sdx = dx//10
    tdx = dx%10
    return fdx+sdx+tdx

# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# n = int(input("Enter a threedigit number: "))
# if n>999 or n<100:
#     print("I say Threedigit number")
# else:
#     fd = n//100
#     d = n-(fd*100)
#     sd = d//10
#     td = d%10
#     print(fd+sd+td)


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, 
# что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# g = int(input("How many cranes did the guys make?"))
# if g % 2 == 0:
#     n1 = g//2
#     n2 = n1//3
#     k = n1+n2
#     ts = n2
#     print (ts,k,ts)
# else:
#     print("Imposile")


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

# t = int(input("Enter the tickets number: "))
# if t>999999 or t<99999:
#     print("This is not the ticket")
# else:
#     h1 = t//1000
#     h2 = t%1000
#     if sum3digit(h1) == sum3digit(h2):
#         print("This is a lucky ticket!")
#     else:
#         print("This isn't a lucky ticket!")


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

# n = int(input("Enter n: "))
# m = int(input("Enter m: "))
# k = int(input("Enter k: "))
# if k < n * m and ((k % n == 0) or (k % m == 0)):
#     print("Yes")
# else:
#     print("No")
   