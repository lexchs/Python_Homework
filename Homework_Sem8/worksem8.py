def show_all_records():
    n = 1
    with open("file.txt", 'r', encoding='utf-8') as f:
        for line in f:
            print(f'{n}-',end='')
            print(*line.strip().split(';'))
            n+=1
     
def add_contact(fio,number):
    with open("file.txt","a",encoding="utf-8") as f:
        f.write("\n")
        f.write(fio.replace(" ",";")+';'+ number)
             
def search_record(searching_data):
    with open("file.txt","r",encoding="utf-8") as f:
        for line in f:
            if searching_data.lower() in line.lower().split(';')[0]:
                print(line.replace(';',' '), end="")

def change_contact(n,newcontact):
    with open ('file.txt', 'r',encoding="utf-8") as f:
        text = f.readlines()
        text[n-1] = newcontact.replace(" ",";")+";""\n"
    with open ('file.txt','w',encoding="utf-8") as f: 
        f.writelines(text)
          
def delete_contact(n):
    with open ('file.txt', 'r',encoding="utf-8") as f:
        text = f.readlines()
        text.pop(n-1)
    with open ('file.txt','w',encoding="utf-8") as f:
        f.writelines(text)
        
def main():
    print("Выберите действие:\n1 - Показать справочник\n2 - Найти контакт\n3 - Добавить контакт\n4 - Изменить контакт\n5 - Удалить контакт")
    select = int(input(""))
    if select == 1:
        show_all_records()
    elif select == 2:
        sd = input("Введите данные для поиска: ")
        search_record(sd)
    elif select == 3:
        new_contact_fio = input("Введите ФИО: ")
        new_contact_number = input("Введите Номер: ")
        add_contact(new_contact_fio,new_contact_number)
    elif select == 4:
        show_all_records()
        sd = int(input("Выберите контакт для редактирования: "))
        nc = input("Введите новые данные для контакта: ")
        change_contact(sd,nc)
    elif select == 5:
        show_all_records()
        n = int(input("Выберите контакт для удаления: "))
        delete_contact(n)


main()