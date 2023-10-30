#!/usr/bin/env python3
import sys

def is_safe(board, row, col, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_nqueens(n):
    def solve_util(board, row):
        if row == n:
            solutions.append([[i, row] for i in range(n)])
            return
        
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                solve_util(board, row + 1)
                board[row][col] = 0

    solutions = []
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve_util(board, 0)
    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(n)
    for solution in solutions:
        print(solution)

