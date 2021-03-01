from variables import ADDRESS_BOOK
from notebook import Notebook, add_note, view_note, update_note, delete_note, get_notes


def main():
    app = Notebook(ADDRESS_BOOK)
    choise = ''
    while choise != '6':

        print(app)
        choice = input('Выбрано: ')
        if choice == '1':
            add_note()
        elif choice == '2':
            view_note()
        elif choice == '3':
            update_note()
        elif choice == '4':
            delete_note()
        elif choice == '5':
            get_notes()
        elif choice == '6':
            print('Вы вышли из приложения')
            break
        else:
            print('Неправильный ключ, повторите попытку')


if __name__ == '__main__':
    main()
