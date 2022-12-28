import os
import shutil
import sys

from victory import start_victory
from account import start_account


def main():
    print('Wellcome to console FileManager!')
    # print(os.getcwd())
    # exit()

    while True:
        print('-------------')
        print('1. создать папку')
        print('2. удалить (файл/папку)')
        print('3. копировать (файл/папку)')
        print('4. просмотр содержимого рабочей директории')
        print('5. посмотреть только папки')
        print('6. посмотреть только файлы')
        print('7. просмотр информации об операционной системе')
        print('8. создатель программы')
        print('9. играть в викторину')
        print('10. мой банковский счет')
        print('11. смена рабочей директории')
        print('12. выход')
        print('-------------')

        choice = input('Выберите пункт меню ')
        if choice == '1':  # создать папку
            dirname = input('Введите имя папки которую создать: ')
            if not os.path.exists(dirname):
                os.mkdir(dirname)
        elif choice == '2':  # удалить (файл/папку)
            filedirname = input('Введите имя файла/папки которую удалить: ')
            if os.path.exists(filedirname):
                if os.path.isdir(filedirname):
                    shutil.rmtree(filedirname)  # dir shutil.rmtree() deletes a directory and all its contents.
                else:
                    os.remove(filedirname)  # file
        elif choice == '3':  # копировать (файл/папку)
            filedirname1 = input('Введите имя файла/папки которую копировать: ')
            filedirname2 = input('Введите имя файла/папки в которую копировать: ')
            if os.path.exists(filedirname1):
                if os.path.isdir(filedirname1):
                    shutil.copytree(filedirname1, filedirname2)  # dir
                else:
                    shutil.copy(filedirname1, filedirname2)  # file
        elif choice == '4':  # просмотр содержимого рабочей директории
            oslist = os.listdir(os.getcwd())
            print(oslist)
        elif choice == '5':  # посмотреть только папки
            oslist = os.listdir(os.getcwd())
            dirlist = list(filter(lambda x: os.path.isdir(x), oslist))
            print(dirlist)
        elif choice == '6':  # посмотреть только файлы
            oslist = os.listdir(os.getcwd())
            filelist = list(filter(lambda x: not os.path.isdir(x), oslist))
            print(filelist)
        elif choice == '7':  # просмотр информации об операционной системе
            sysinfo = f'My OS is {sys.platform} ({os.name})'
            print(sysinfo)
        elif choice == '8':  # создатель программы
            name = 'WarLock888'
            info = f'Program created by {name}'
            print(info)
        elif choice == '9':  # играть в викторину
            start_victory()
        elif choice == '10':  # мой банковский счет
            start_account()
        elif choice == '11':  # смена рабочей директории
            dirname = input('Введите имя директории на которую менять рабочую директорию: ')
            if os.path.exists(dirname):
                os.chdir(dirname)
            else:
                print(f'Ошибка. Нет такой директории.')
        elif choice == '12':  # выход
            break
        else:
            print('Неверный пункт меню')


if __name__ == '__main__':
    main()
