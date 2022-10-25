
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

number1 = '10006'

def get_name_by_number(number1):

    for doc in documents:
        if doc['number'] == number1:
            ppp = print('{0}'.format(doc['name']))
            return (ppp)
    else:
        return ('Отсутствуют документы с таким номером\n')


def show_documents():
    for doc in documents:
        lll = print(doc['type'], doc['number'], doc['name'])
    for key, values in directories.items():
        lll_2 = print(key, '->', values)         
    return (lll, lll_2)
        

def get_directory_by_number():
    number = '2207 876234'
    for directory, list_docs in directories.items():
        if number in list_docs:
            sss = print('Документ с номером {0} находится на полке {1}'.format(number, directory))
            return (sss)
    else:
        return ('Отсутствуют документы с таким номером')


number_3 = '8-800-555-3535'
name_3 = 'Leo Doveberg'
doc_type_3 = 'invoice'
directory_number_3 = '3'

def add_document(number, name, doc_type, directory_number):
    if number and name and doc_type and directory_number:
        documents.append({"type": doc_type, "number": number, "name": name})
        if directory_number in directories:
            directories[directory_number].append(number)
            return ('Запись добавлена на существующую полку')
        else:
            directories[directory_number] = [number]
            return ('Запись добавлена на новую полку')
    else:
        return('ВНИМАНИЕ! Введены не все данные')

person_number_4 = '8-800-555-3535'

def remove_document(person_number):
    bookshelf = ''
    for elem in documents:
        if elem['number'] == person_number:
            documents.remove(elem)
    for number_shelf, number_documents in directories.items():
        if person_number in number_documents:
            number_documents.remove(person_number)
            bookshelf = number_shelf
    return('Документ удален из базы данных и убран с полки')


def main(command):
    while True:
        #command = input('Введите команду: ')
        if command == 'p':
            get_name_by_number(number1)
            print('\n')
            break
        elif command == 'l':
            show_documents()
            print('\n')
            break
        elif command == 's':
            get_directory_by_number()
            print('\n')
            break
        elif command == 'a':
            add_document(number_3, name_3, doc_type_3, directory_number_3)
            print('\n')
            break
        elif command == 'd':
            remove_document(person_number)
            print('\n')
            break
        elif command == 'e':
            break

pp = 'p'
ll = 'l'
ss = 's'
aa = 'a'
dd = 'd'

main(pp)
main (ll)
main (ss)
main (aa)
main (ll)
main (dd)
main (ll)