import fileinput
from variables import HELP_TEXT

class Person:
    def __init__(
        self,
        first_name: str = None,
        last_name: str = None,
        company: str = None,
        phone: str = None,

    ) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.phone = phone

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name} {self.company} {self.phone}'

class Notebook:
    def __init__(self, address_book: list = None) -> None:
        if address_book is None:
          address_book = []
          notes_id = {}
        else:
          notes_id = {note['phone_number'] for note in address_book}
        self.address_book = address_book
        self.notes_id = notes_id

    def __str__(self) -> str:
        return HELP_TEXT

    def add_note(self) -> None:
        first_name, last_name, company, phone = self.get_details_about_person()
        record = '{} {} {} {}'.format(first_name, last_name, company, phone)
        print(record)
        f = open('notebook.txt', 'a')
        f.write(record + '\n')
        f.close()

    def get_details_about_person(self)->tuple:
        first_name = input('Имя: ')
        last_name = input('Фамилия: ')
        company = input('Компания: ')
        phone = input('Телефон: ')
        return first_name, last_name, company, phone

    def get_notes(self):
        f = open('notebook.txt', 'r')
        print(f.read())
        f.close()

    def view_note(self):
        phone = str(input('Введите номер телефона: '))
        with open('notebook.txt', 'r') as f:
            for line in f:
                if phone in line:
                    print(line) #не знаю как обработать случай Номер не найден, как ниже работает коряво'
                    break
                #else:
                    #print(Номер телефона не найден')

    def update_note(self):
        phone = str(input('Введите номер телефона изменяемой записи: '))
        for line in fileinput.input('notebook.txt', inplace=True):
            if phone in line:
                continue
            print(line.rstrip('\n'))
        print('Введите новые данные')
        first_name, last_name, company, phone = self.get_details_about_person()
        record = '{} {} {} {}'.format(first_name, last_name, company, phone)
        print(record)
        f = open('notebook.txt', 'a')
        f.write(record + '\n')
        f.close()

    def delete_note(self):
        phone = str(input('Введите номер телефона: '))
        for line in fileinput.input('notebook.txt', inplace=True):
            if phone in line:
                continue
            print(line.rstrip('\n'))  # тоже не знаю как сделать обработку краевых случаев