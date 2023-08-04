#!/usr/bin/python3
""" n queens """

import sys


def printBoard(board):
    """ print the board """
    print("[", end="")
    for row in board:
        print("[", end="")
        for col in row:
            print(col, end=", ")
        print("\b\b],")
    print("\b]")


def isSafe(board, row, col):
    """ checks if a queen can be placed on board[row][col] """
    for c in range(col):
        if board[row][c] == 1:
            return False

    for r, c in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[r][c] == 1:
            return False

    for r, c in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[r][c] == 1:
            return False

    return True


def solveNQUtil(board, col):
    """ recursive utility function to solve N Queen problem """
    if col == len(board):
        printBoard(board)
        return True

    res = False
    for row in range(len(board)):
        if isSafe(board, row, col):
            board[row][col] = 1
            res = solveNQUtil(board, col + 1) or res
            board[row][col] = 0

    return res


def solveNQ(n):
    """ solve N Queen problem """
    if n < 4:
        print("N must be at least 4")
        return False

    board = [[0 for col in range(n)] for row in range(n)]
    solveNQUtil(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solveNQ(n)