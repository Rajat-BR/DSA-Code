#Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
matrix = [
    [1, 1, 1], 
    [1, 0, 1],
    [1, 1, 1]
]

def setzeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    rowset = set()
    colset = set() 
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                rowset.add(i)
                colset.add(j)

    for i in range(rows):
        for j in range(cols):
            if i in rowset or j in colset:
                matrix[i][j] = 0

    return matrix

print(setzeroes(matrix))
