# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# n = []
# k = int(input("How many?: "))
# count = 0
# for i in range(k):
#     n.append(int(input("Number?: ")))
# m = int(input("Cho ischesh?: "))
# for i in n:
#     if i == m:
#         count+=1
# print(count)

# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# sp = []
# sp1 = []
# count = 0
# for i in range( int(input("List size: "))):
#     sp.append(int(input("Number: ")))
# m = int(input("Nearest number: "))
# for i in sp:
#     n = i - m
#     if n<0:
#         n*=(-1)
#     sp1.append(n)
# res = sp[sp1.index(min(sp1))]
# for i in sp1:
#     if i == min(sp1):
#         count +=1
# tempI = sp1.index(min(sp1))
# if count >1:
#     sp1[tempI] = sp1[tempI] * 10
#     res1 = sp[sp1.index(min(sp1))]
#     print(f"{res}, {res1}")
# else:
#     print(res)


# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; 
# B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; 
# K – 5 очков; 
# J, X – 8 очков; 
# Q, Z – 10 очков. 
# А русские буквы оцениваются так: 
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, 
# которое содержит либо только английские, либо только русские буквы.
# *Пример:*
# ноутбук
#     12

# d = {"АВЕИНОРСТAEIOULNSTR": 1, "ДКЛМПУDG": 2, "БГЁЬЯBCMP": 3, "ЙЫFHVWY": 4, "ЖЗХЦЧK": 5,"ШЭЮJX": 8, "ФЩЪQZ": 10}
# b = input("Введите слово: ").upper()
# l = list(b)
# res = 0
# for i in range(len(l)):
#     for key, value in d.items():
#         if l[i] in key: res = value + res
# print(res)
    
    
    