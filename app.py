# Sudoku Solver using Backtracking

# Rulesets
# N = Normal Sudoku Rules Apply
# H = Anti-Knight
# K = Anti-King
# Q = Anti-Queen
# D = Diagonal
# W = Windoku

def isValidPlacement(test_puzzle, pos, testnum, ruleset):
### Tests a placement against the ruleset ###
    if "N" in ruleset:
        # Normal Sudoku Rules

        # Check Row
        if testnum in test_puzzle[pos[0]]:
            return False

        # Check Column
        if testnum in [test_puzzle[row][pos[1]] for row in range(9)]:
            return False

        # Check House
        house = 3 * (pos[0] // 3) + (pos[1] // 3)
        house_start = house//3 * 3, house%3 * 3
        for hr in range(3):
            for hc in range(3):
                if testnum == test_puzzle[house_start[0] + hr][house_start[1] + hc]:
                    return False
    return True


def solve(puzzle, ruleset):
    test_puzzle = []
    solutions = []
    solved = True

    #copy puzzle into the test
    for row in range(9):
        if solved and 0 in puzzle[row]:
            solved = False
        test_puzzle.append([n for n in puzzle[row]])
    if solved:
        return test_puzzle

    for row in range(9):
        for col in range(9):
            if test_puzzle[row][col] is not 0:
                pass
            for testnum in range(1,10):
                if isValidPlacement(test_puzzle, (row, col), testnum, ruleset):
                    solve(test_puzzle, ruleset)
            pass
    return []


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

    print(solve(puzzle, "N"))

main()