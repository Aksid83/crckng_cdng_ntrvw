"""
Write an algorithm such that if an element in an MxN matrix is 0,
its entire row and column are set to 0.
"""


def set_zeroes(matrix):
    row = [False for r in range(len(matrix))]
    column = [False for c in range(len(matrix[0]))]
    print('Initial matrix:')
    for el in matrix:
        print(el)
    print('\n')
    # Store the row and column index with value 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row[i] = True
                column[j] = True

    # Nullify rows
    for i in range(len(row)):
        if row[i]:
            nullify_row(matrix, i)

    # Nullify columns
    for j in range(len(column)):
        if column[j]:
            nullify_column(matrix, j)
    print('Zeroed matrix:')
    for el in matrix:
        print(el)


def nullify_row(matrix, row):
    for j in range(len(matrix[0])):
        matrix[row][j] = 0


def nullify_column(matrix, column):
    for i in range(len(matrix)):
        matrix[i][column] = 0


mtrx = [[1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2],
        [3, 3, 0, 3, 3],
        [4, 4, 4, 4, 4],
        [5, 5, 5, 5, 5]]

set_zeroes(mtrx)
