#!/usr/bin/python3
''' nQueens problem.
'''

from sys import argv, exit


N = 0


def isSafe(board, row, col):
    ''' Checks if a square is safe
    '''
    for i in range(col):
        if board[row][i]:
            return False

    for j in range(row):
        if board[j][col]:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    for i, j in zip(range(row + 1, N, 1), range(col - 1, -1, -1)):
        if board[i][j]:
            return False

    return True


def nQueens(board, col):
    ''' Returns an array containing the positions of the queen
    '''

    if col >= N:
        sol = []
        for i in range(N):
            for j in range(N):
                if board[i][j]:
                    sol.append([i, j])
        print(sol)
        return

    for i in range(N):
        if isSafe(board, i, col):
            board[i][col] = 1
            nQueens(board, col + 1)
            board[i][col] = 0


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        N = int(argv[1])
        if N < 4:
            print("N must be at least 4")
            exit(1)
        board = [[0] * N for _ in range(N)]
        nQueens(board, 0)
    except ValueError:
        print("N must be a number")
        exit(1)
