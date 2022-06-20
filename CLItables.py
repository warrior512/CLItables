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


def getMaxLens(tabList):
    maxItemsLens = [len(i) for i in tabList[0]]
    for row in tabList:
        for i in range(len(maxItemsLens)):
            if len(row[i]) > maxItemsLens[i]:
                maxItemsLens[i] = len(row[i])
    return maxItemsLens


def printTable(tabList, tabName):
    maxItemsLens = getMaxLens(tabList)
    print(f'table: {tabName}\n')
    cnt = 0
    for line in tabList:
        index = 0
        if cnt == 1:
            print('-' * (sum(maxItemsLens) + len(maxItemsLens) + 2 + len(str(len(tabList))) - 1))
        if cnt == 0:
            print('#  '.rjust(2 + len(str(len(tabList))), ' '), end ='')
        else:
            print((str(cnt) + '| ').rjust(2 + len(str(len(tabList))), ' '), end ='')
        for i in line:
            print(i.ljust(maxItemsLens[index], ' '), end = ' ')
            index += 1
        print()
        cnt += 1
    print('-' * (sum(maxItemsLens) + len(maxItemsLens) + 2 + len(str(len(tabList))) - 1))
    print(f'columns: {str(len(tabList[0]))}  rows: {str(len(tabList) - 1)}')


def addRow(tabList):
    row = []
    index = input('after row (enter for add row to end): ').strip()
    if not index.isdigit() and index != '' or index.isdigit() and int(index) > len(tabList) - 1:
        print('>>> invalid value')
        input()
        return tabList
    elif index == '':
        index = str(len(tabList))
    for key in tabList[0]:
        value = input(key + ': ')
        row.append(value)
    tabList.insert(int(index) + 1, row)
    return tabList


def fileToList(tabName):
    with open(f'{getSelfPath()}{tabFold}/{tabName}.csv') as f:
        return list(csv.reader(f))


def exitTab(tabList, tabName):
    if fileToList(tabName) != tabList:
        while True:
            item = input('save changes? [y/n]:').lower().strip()
            if item == 'y':
                createFile(tabName, tabList)
                print(f'>>> table {tabName} was saved')
                return
            elif item == 'n':
                return
            else:
                print('>>> command not found')


def openTable(tabName):
    if not os.path.isfile(f'{getSelfPath()}{tabFold}/{tabName}.csv'):
        print('>>> table not found')
        return
    tabList = fileToList(tabName)
    while True:
        printLogo()
        printTable(tabList, tabName)
        printOpenMenu()
        action = input('>').lower().strip()
        if action == 'ar':
            flist = addRow(tabList)
        elif action == 's':
            createFile(tabName, tabList)
            print(f'>>> table {tabName} was saved')
            input()
        elif action == 'x':
            exitTab(tabList, tabName)
            return


if __name__ == '__main__':
    createTablesFolder()
    while True:
        printLogo()
        os.system(f'ls {getSelfPath()}{tabFold}') 
        printMainMenu()
        action = input('> ').lower().strip()
        if action == 'n':
            tableName = input('new table name: ')
            print(createNewTable(f'{tableName}'))
            input('\npress enter to continue')
            continue
        elif action == 'o':
            openTable(input('open table name: ').strip())
            
        elif action == 'x':
            exit()












