def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row)))

def is_valid_move(grid, row, col, num):
    # Check the row and column for the same number
    if num in grid[row] or num in [grid[i][col] for i in range(9)]:
        return False

    # Check the 3x3 region for the same number
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True

def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

# Example Sudoku puzzle (0 represents empty cells)
sudoku_grid = [
    [0, 0, 0, 0, 0, 0, 3, 0, 0],
    [4, 0, 8, 0, 6, 0, 0, 0, 0],
    [0, 2, 6, 0, 1, 0, 0, 7, 0],
    [0, 1, 2, 0, 0, 5, 7, 6, 0],
    [0, 0, 0, 0, 3, 0, 0, 0, 0],
    [0, 6, 7, 9, 0, 0, 5, 4, 0],
    [0, 5, 0, 0, 7, 0, 6, 3, 0],
    [0, 0, 0, 0, 5, 0, 8, 0, 1],
    [0, 0, 9, 0, 0, 0, 0, 0, 0]
]

if solve_sudoku(sudoku_grid):
    print("Solved Sudoku:")
    print_grid(sudoku_grid)
else:
    print("No solution exists.")
