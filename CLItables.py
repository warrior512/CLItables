import csv
from modules.interface import *


tabFold = 'tables'


def getSelfPath():
    selfPath = os.path.abspath(__file__)
    selfName = os.path.basename(selfPath)
    return selfPath[:-len(selfName)]


def createTablesFolder():
    foldPath = f'{getSelfPath()}{tabFold}'
    if not os.path.isdir(foldPath):
        os.system(f'mkdir {foldPath}')


def createFile(tabName, tabList):
    fileAbsPath = f'{getSelfPath()}{tabFold}/{tabName}.csv'
    os.system(f'touch {fileAbsPath}')
    with open(f'{fileAbsPath}', 'w') as f:
        for row in tabList:
            csv.writer(f).writerow(row)
        


def createNewTable(newTableName):
    if not newTableName.isalnum():
        return '\n>>> invalid filename'
    elif os.path.isfile(f'{getSelfPath()}{tabFold}/{newTableName}.csv'):
        return f'\n>>> table {newTableName} already exists'
    else:
        while True:
            columns = input('number of columns: ').strip()
            if not columns.isdigit():
                print('>>> enter digit')
                continue
            else:
                break
        newTabList = []
        for i in range(int(columns)):
            newTabList.append(input(f'culumn {i + 1}: '))
        createFile(newTableName, [newTabList])
        return f'\n>>> table {newTableName} created'


if __name__ == '__main__':
    createTablesFolder()
    while True:
        print_logo()
        os.system(f'ls {getSelfPath()}{tabFold}') 
        main_menu()
        action = input('> ').lower().strip()
        if action == 'n':
            tableName = input('new table name: ')
            print(createNewTable(f'{tableName}'))
            input('\npress enter to continue')
            continue
        elif action == 'x':
            exit()












