

def printBoard(n, board):

        for i in range(n):
            for j in range(n):
                print(board[i][j], end="  ")
            print()

def canPlaceQueen(n, board, i, j):

    #check for the column:

    for row in range(0, i):

        if board[row][j] == 1:
            return False


    x, y =  i, j

    while x>=0 and y>=0:

        if board[x][y] == 1:
            return False

        x -= 1
        y -= 1


    x, y = i, j

    while x>=0 and y < n:

        if board[x][y] == 1:
            return False

        x -= 1
        y += 1

    return True

def solveNQueen(n, board, i):
    '''
    :param n: size of board
    :param board: chess board of size n*n
    :param i: current row
    :return: True or False
    '''
    # base case
    if i == n:
        printBoard(n, board)
        return True

    # Recurive Case

    for j in range(0, n):

        if canPlaceQueen(n, board, i, j) == True:

            board[i][j] = 1

            success = solveNQueen(n, board, i+1)

            if success == True:
                return True

            # Backtracking
            board[i][j] = 0

    return False


n = 30

board = [[0 for i in range(n)] for j in range(n)]

print('Initial Board: ', printBoard(n, board))

solveNQueen(n, board, 0)
