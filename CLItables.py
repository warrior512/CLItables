from modules.interface import *


def getSelfPath():
    selfPath = os.path.abspath(__file__)
    selfName = os.path.basename(selfPath)
    return selfPath[:-len(selfName)]


def createTablesFolder():
    if not os.path.isdir(f'{getSelfPath()}tables'):
        os.system(f'mkdir {getSelfPath()}tables')


if __name__ == '__main__':
    createTablesFolder()
    print_logo()
    os.system(f'ls {getSelfPath()}tables') 
    main_menu()
