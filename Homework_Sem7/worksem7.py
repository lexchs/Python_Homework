# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, 
# то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите 
# “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# пара-ра-рам рам-пам-папам па-ра-па-да

# def search_rhythm(phrase:str):    
#     vowel_list = ['а','я','у','ю','о','е','ё','э','и','ы']
#     words = phrase.split()
#     vowel_of_word = []
#     for i in range(len(words)):
#         count = 0
#         for char in range(len(list(words[i]))):
#             if list(words[i])[char] in vowel_list:
#                 count +=1
#         vowel_of_word.append(count)
#     if len(set(vowel_of_word)) == 1:
#         print('Парам пам-пам')
#     else:
#         print('Пам парам')

# poem = input("Напиши стих: ")
# search_rhythm(poem)


# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, 
# вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print(operation(i, j), end='\t')
        print()


print_operation_table(lambda x, y: x * y, num_rows=8, num_columns=6)


        
