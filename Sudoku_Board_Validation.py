'''
Sudoku board validation algorithm
You have been tasked with developing an algorithm to validate a 9 x 9 Sudoku board. Your algorithm needs to verify the validity of the filled cells on the board, adhering to the following conditions:

Every row should contain the numbers 1-9 exactly once, without repetition.
Every column should contain the numbers 1-9 exactly once, without repetition.
Each of the nine 3 x 3 sub-boxes within the grid should contain the numbers 1-9 exactly once, without repetition.

Can you outline an algorithm or a step-by-step approach to determine if the given Sudoku board configuration is valid based on these conditions?

Important Note: Ensure that you save your solution before progressing to the next question and before submitting your answer.

Exercise-1

Input :

9
5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9

Output :

YES

Exercise-2

Input:

9
5 3 . . 7 . . . .
5 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9

Output:
NO
'''

#CODE:

import sys

def is_valid_set(lst):
    seen = set()
    for num in lst:
        if num != '.':
            if num in seen:
                return False
            seen.add(num)
    return True
    
def is_valid_sudoku(size, board):
    # Check Rows
    for row in board:
        if not is_valid_set(row):
            return "NO"

    # Check Columns
    for col in zip(*board):
        if not is_valid_set(col):
            return "NO"

    # Check Sub-boxes
    for i in range(0, size, 3):
        for j in range(0, size, 3):
            sub_box = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if not is_valid_set(sub_box):
                return "NO"

    # All conditions satisfied
    return "YES"

size = int(input())
board = []
for i in range(size):
    row = input()
    board.append(row.split())
    for ele in board[i]:
        if 48 <= ord(ele) <= 57:
            board[i][board[i].index(ele)] = int(ele)
        
outputVal = is_valid_sudoku(size,board)
print (outputVal)