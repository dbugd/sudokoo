import random
from pprint import pprint

def is_safe(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False

    for x in range(9):
        if grid[x][col] == num:
            return False
 
    for i in range(3):
        for j in range(3):
            if grid[(row//3)*3 + i][(col//3)*3 + j] == num:
                return False
    return True

def solve_sudoku(grid, row, col):
    N = 9
    if (row == N - 1 and col == N):
        return True

    if col == N:
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solve_sudoku(grid, row, col + 1)

    nums = [1,2,3,4,5,6,7,8,9]
    random.shuffle(nums)
    for num in nums:
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False

def remove_from_sudoku(grid):
    levels = [(17, 20), (21, 30), (31, 40), (41, 50), (51, 60), (61, 70), (71, 75)]
    weights = [1, 10, 25, 35, 20, 8, 1]
    i = random.randint(*random.choices(levels, weights = weights)[0])
    pairs = random.sample([(x, y) for x in range(9) for y in range(9)], 81 - i)
    for x,y in pairs:
        grid[x][y] = 0
    return grid

def generate_sudoku():
    grid = [[0 for _ in range(9)] for _ in range(9)]
    solve_sudoku(grid, 0, 0)
    grid_sol = [a[:] for a in grid]
    remove_from_sudoku(grid)
    return grid_sol, grid
