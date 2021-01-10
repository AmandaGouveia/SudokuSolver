# Sudoku Solver using Backtracking

def solve(puzzle):
    test = []

    #copy puzzle into the test
    for row in range(9):
        test.append([n for n in test[row]])

    for row in range(9):
        for col in range(9):

            pass

def main():
    print("Sudoku Solver")
    puzzle = [
        [5, 3, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 2, 7, 1, 3, 0, 0, 0, 0],
        [0, 9, 0, 3, 2, 8, 0, 5, 0],
        [0, 1, 0, 4, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 4],
        [0, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 4, 0, 6, 0],
        [3, 0, 0, 0, 0, 0, 9, 0, 0]
    ]

    correct = [
        [
            [5, 3, 1, 8, 4, 9, 6, 7, 2],
            [6, 4, 9, 5, 7, 2, 8, 3, 1],
            [8, 2, 7, 1, 3, 6, 5, 4, 9],
            [4, 9, 6, 3, 2, 8, 1, 5, 7],
            [2, 1, 8, 4, 5, 7, 3, 9, 6],
            [7, 5, 3, 9, 6, 1, 2, 8, 4],
            [9, 6, 2, 7, 8, 3, 4, 1, 5],
            [1, 8, 5, 2, 9, 4, 7, 6, 3],
            [3, 7, 4, 6, 1, 5, 9, 2, 8]
        ]
    ]
