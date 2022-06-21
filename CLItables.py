import csv
from datetime import datetime
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
        writeLog('create tables folder')


def getlogFilePath():
    return f'{getSelfPath()}log.txt'


def crateLogFile():
    logTime = datetime.now().strftime('[%d-%m-%Y %H:%M:%S]')
    if not os.path.isfile(getlogFilePath()):
        with open(getlogFilePath(), 'w') as f:
            f.write(f'{logTime} create log.txt\n')


def writeLog(log):
    logTime = datetime.now().strftime('[%d-%m-%Y %H:%M:%S]')
    with open(getlogFilePath(), 'a') as f:
        f.write(f'{logTime} {log}\n')


def createFile(tabName, tabList):
    fileAbsPath = f'{getSelfPath()}{tabFold}/{tabName}.csv'
    os.system(f'touch {fileAbsPath}')
    with open(f'{fileAbsPath}', 'w') as f:
        for row in tabList:
            csv.writer(f).writerow(row)
        

def fileToList(tabName):
    with open(f'{getSelfPath()}{tabFold}/{tabName}.csv') as f:
        return list(csv.reader(f))


def createNewTable(newTableName):
    if not newTableName.isalnum():
        return '>>> invalid filename'
    elif os.path.isfile(f'{getSelfPath()}{tabFold}/{newTableName}.csv'):
        return f'>>> table {newTableName} already exists'
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
        writeLog(f'create new table "{newTableName}"')
        return f'>>> table {newTableName} created'


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


def addRow(tabName, tabList):
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
    writeLog(f'add row {row} in table "{tabName}"')
    return tabList


def editRow(tabList, tabName):
    edRow = input('edit row, "0" to rename columns: ').strip()
    if not edRow.isdigit() or edRow.isdigit() and int(edRow) > len(tabList) - 1:
        input('>>> invalid value')
        return tabList
    befRow = tabList[int(edRow)].copy()
    index = 0
    print('"-" do dont edit value')
    for key in tabList[0]:
        editVal = input(f'{key} "{tabList[int(edRow)][index]}" edit to: ')
        if editVal == '-':
            tabList[int(edRow)][index] = tabList[int(edRow)][index]
        else:
            tabList[int(edRow)][index] = editVal
        index += 1
    writeLog(f'edit row #{edRow} on table "{tabName}". before: {befRow}; after: {tabList[int(edRow)]}')
    return tabList


def delRow(tabList, tabName):
    print(tabList)
    delRow = input('delete row:').strip()
    if not delRow.isdigit() or delRow.isdigit() and int(delRow) > len(tabList) - 1 or delRow == '0':
        input('>>> invalid value')
        return tabList
    deletedRow = tabList[int(delRow)].copy()
    del tabList[int(delRow)]
    writeLog(f'delete row#{delRow} on table "{tabName}": {deletedRow}')
    return tabList


def addColumn(tabList, tabName):
    while True:
        addColInd = input(f'number column add (1-{str(len(tabList[0]) + 1)}): ').strip()
        if not addColInd.isdigit() or addColInd.isdigit() and int(addColInd) > len(tabList[0]) + 1 or addColInd.isdigit() and int(addColInd) < 1:
            input('>>> invalid value')
            return
        addColInd = int(addColInd)
        break
    while True:
        addColName = input('new column name: ').strip()
        if addColName in tabList[0]:
            input('>>> invalid value')
            continue
        break
    for line in tabList:
        if line == tabList[0]:
            line.insert(addColInd - 1, addColName)
        else:
            line.insert(addColInd - 1, '')
    writeLog(f'add column: "{addColName}" in table "{tabName}"')
    return tabList


def exitTab(tabList, tabName):
    if fileToList(tabName) != tabList:
        while True:
            item = input('save changes? [y/n]:').lower().strip()
            if item == 'y':
                createFile(tabName, tabList)
                writeLog(f'exit on table "{tabName}" with saving')
                print(f'>>> table {tabName} was saved')
                return
            elif item == 'n':
                writeLog(f'exit on table "{tabName}" without saving')
                return
            else:
                print('>>> command not found')


def openTable(tabName):
    if not os.path.isfile(f'{getSelfPath()}{tabFold}/{tabName}.csv'):
        print('>>> table not found')
        return
    writeLog(f'open table "{tabName}"')
    tabList = fileToList(tabName)
    while True:
        printLogo()
        printTable(tabList, tabName)
        printOpenMenu()
        action = input('>').lower().strip()
        if action == 'ar':
            flist = addRow(tabName, tabList)
        elif action == 'er':
            editRow(tabList, tabName)
        elif action == 'dr':
            tabList = delRow(tabList, tabName)
        elif action == 'ac':
            addColumn(tabList, tabName)
        elif action == 's':
            createFile(tabName, tabList)
            writeLog(f'save table "{tabName}"')
            input(f'>>> table {tabName} was saved')
        elif action == 'x':
            exitTab(tabList, tabName)
            writeLog(f'exit from {tabName} table')
            return
        else:
            input('>>> command not found')


def delTable():
    tabName = input('file name: ').strip()
    tabPath = f'{getSelfPath()}{tabFold}/{tabName}.csv'
    if not os.path.isfile(tabPath):
        print('>>> file not found')
        input()
        return
    os.system(f'rm {tabPath}')
    writeLog(f'delete table "{tabName}"')
    input(f'>>> table "{tabName}" deleted')


if __name__ == '__main__':
    crateLogFile()
    createTablesFolder()
    writeLog('start CLItables')
    while True:
        printLogo()
        os.system(f'ls {getSelfPath()}{tabFold}') 
        printMainMenu()
        action = input('> ').lower().strip()
        if action == 'n':
            tableName = input('new table name: ')
            print(createNewTable(f'{tableName}'))
            input('press enter to continue')
            continue
        elif action == 'o':
            openTable(input('open table name: ').strip())   
        elif action == 'x':
            writeLog('exit from the program')
            exit()
        elif action == 'd':
            delTable()
        else:
            input('>>> command not found')












