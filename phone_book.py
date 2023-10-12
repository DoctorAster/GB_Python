def check_row_data(row_data):

    return

def get_row_data(message):
    print(message)
    f_name = input('Имя: ').title()
    s_name = input('Отчество: ').title()
    l_name = input('Фамилия: ').title()
    phone_num = input('Номер телефона: ')
    row_data = l_name + ', ' + f_name + ', ' + s_name + ', ' + phone_num
    return row_data

def find_exac_row(file_db, row_data):
    text = read_file(file_db)
    if row_data in text:
        return True
    else:
        return False
    
def add_row(file_db):
    message = 'Ввод новых данных'
    row_data = get_row_data(message)
    if find_exac_row(file_db, row_data):
        print('Такая запись уже имеется')
        return False
    else:
        row_data = "\n" + row_data
        phone_book = open(file_db, 'a')
        phone_book.write(row_data)
        phone_book.close()
        print('Добавлена новая запись: ')
        print (row_data)
        return True

def del_row(file_db, row_data):

    return

def read_file(file_db):
    phone_book = open(file_db, 'r')
    text = ''
    for row in phone_book.read():
        text = text + row
    phone_book.close()
    return text

def read_row(file_db, row_data):


    return

def check_choce(selected):
    right_choices = ('1', '2', '3', '4')
    if selected in right_choices:
        return True
    else:
        print('Нет такого пункта меню! Выберите снова.')
        return False

def main_menu():
    text = ''
    print("   -= Главное меню =-")
    print("---------------------")
    print('1 - Показать всех')
    print('2 - Добавить запись')
    print('3 - Искать данные')
    print('4 - Удалить данные')
    choice = input("Ваш выбор: ")
    if check_choce(choice): 
        print(choice)
        if choice=='1':
            text = read_file(File_db)
            
            print (text)
        #           full_text = read_file(phone_book)
        elif choice=='2':
            row_added = add_row(File_db)

        elif choice=='3':
            message = 'Введите данные для поиска: '
            row_data = get_row_data(message)
        elif choice=='4':
            message = 'Введите данные для удаления: '
            row_data = get_row_data(message)
                        
    else: return


    return


File_db = 'phone_book.txt'
main_menu()
