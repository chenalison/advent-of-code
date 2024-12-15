def gridsearch(grid, row, col):
    if ((grid[row-1][col-1] == 'M' and grid[row+1][col+1] == 'S') or\
    (grid[row-1][col-1] == 'S' and grid[row+1][col+1] == 'M')) and\
    ((grid[row+1][col-1] == 'M' and grid[row-1][col+1] == 'S') or\
    (grid[row+1][col-1] == 'S' and grid[row-1][col+1] == 'M')):
        return True
    return False

grid = []

with open("day4/input", "r") as fd:
    for line in fd:
        grid.append(line.strip())

count = 0
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[0])-1):
        if grid[i][j] == 'A':
            count += gridsearch(grid, i, j)

print("X-MAS appears {} times".format(count))