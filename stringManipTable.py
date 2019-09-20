def printTable(tableData):
    colWidth = [0] * len(tableData)
    
    for i in range(len(tableData)):
        for j in range(len(tableData)):
            if len(tableData[i][j]) > colWidth[i]:
                colWidth[i] = len(tableData[i][j])
                
    for x in range(len(tableData[0])):
        for y in range(len(tableData)):
            print(tableData[y][x].rjust(colWidth[y]), end = ' ')
        print('')

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
