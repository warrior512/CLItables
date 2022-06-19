from modules.interface import *


tabFold = 'tables'


def getSelfPath():
    selfPath = os.path.abspath(__file__)
    selfName = os.path.basename(selfPath)
    return selfPath[:-len(selfName)]


def createTablesFolder():
    if not os.path.isdir(f'{getSelfPath()}{tabFold}'):
        os.system(f'mkdir {getSelfPath()}{tabFold}')


def createNewTable(newTableName):
    if os.path.isfile(f'{getSelfPath()}{tabFold}/{newTableName}'):
        return f'{newTableName} already exists'
    elif os.system(f'touch {getSelfPath()}{tabFold}/{newTableName}') != 0:
        return 'invalid filename'
    



if __name__ == '__main__':
    createTablesFolder()
    while True:
        print_logo()
        os.system(f'ls {getSelfPath()}{tabFold}') 
        main_menu()
        action = input('> ').lower().strip()
        if action == 'n':
            tableName = input('new table name: ')
            print(createNewTable(f'{tableName}.csv')
            input('press enter to continue')
            continue
        else:
            continue
