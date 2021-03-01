from variables import ADDRESS_BOOK
from notebook import Notebook

def main():
    app = Notebook(ADDRESS_BOOK)
    choise = ''
    while choise != '6':

        print(app)
        choice = input('Выбрано: ')
        if choice == '1':
            app.add_note()
        elif choice == '2':
            app.view_note()
        elif choice == '3':
            app.update_note()
        elif choice == '4':
            app.delete_note()
        elif choice == '5':
            app.get_notes()
        elif choice == '6':
            print('Вы вышли из приложения')
            break
        else:
            print('Неправильный ключ, повторите попытку')

if __name__ == '__main__':
    main()

