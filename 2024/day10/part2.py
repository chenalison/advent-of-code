# multisource bfs
from collections import deque as queue

grid = []
with open("day10/input", "r") as fd:
    for line in fd:
        grid.append(list(line.strip()))

grid = [[int(x) for x in line] for line in grid]

def helper(grid, row, col, curr):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return False
    if grid[row][col] != curr + 1:
        return False
    if grid[row][col] == 9:
        return True    

    return helper(grid, row-1, col, grid[row][col]) +\
    helper(grid, row+1, col, grid[row][col]) +\
    helper(grid, row, col-1, grid[row][col]) +\
    helper(grid, row, col+1, grid[row][col])

def scoreTrailhead(grid, row, col):
    return helper(grid, row-1, col, grid[row][col]) +\
    helper(grid, row+1, col, grid[row][col]) +\
    helper(grid, row, col-1, grid[row][col]) +\
    helper(grid, row, col+1, grid[row][col])

total = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0:
            score = scoreTrailhead(grid, i, j)
            total += score
            # print(i, j, score)

print("sum of trailhead scores: ", total)