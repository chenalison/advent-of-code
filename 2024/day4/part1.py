
def searchLeft(grid, row, col):
    if col-3 >= 0 and \
        grid[row][col-1] == 'M' and \
        grid[row][col-2] == 'A' and \
        grid[row][col-3] == 'S':
        return True
    return False

def searchLeftUp(grid, row, col):
    if row-3 >= 0 and col-3 >= 0 and \
        grid[row-1][col-1] == 'M' and \
        grid[row-2][col-2] == 'A' and \
        grid[row-3][col-3] == 'S':
        return True
    return False

def searchUp(grid, row, col):
    if row-3 >= 0 and \
        grid[row-1][col] == 'M' and \
        grid[row-2][col] == 'A' and \
        grid[row-3][col] == 'S':
        return True
    return False

def searchRightUp(grid, row, col):
    if row-3 >= 0 and col+3 < len(grid[0]) and \
        grid[row-1][col+1] == 'M' and \
        grid[row-2][col+2] == 'A' and \
        grid[row-3][col+3] == 'S':
        return True
    return False

def searchRight(grid, row, col):
    if col+3 < len(grid[0]) and \
        grid[row][col+1] == 'M' and \
        grid[row][col+2] == 'A' and \
        grid[row][col+3] == 'S':
        return True
    return False

def searchRightDown(grid, row, col):
    if row+3 < len(grid) and col+3 < len(grid[0]) and \
        grid[row+1][col+1] == 'M' and \
        grid[row+2][col+2] == 'A' and \
        grid[row+3][col+3] == 'S':
        return True
    return False

def searchDown(grid, row, col):
    if row+3 < len(grid) and \
        grid[row+1][col] == 'M' and \
        grid[row+2][col] == 'A' and \
        grid[row+3][col] == 'S':
        return True
    return False

def searchLeftDown(grid, row, col):
    if row+3 < len(grid) and col-3 >= 0 and \
        grid[row+1][col-1] == 'M' and \
        grid[row+2][col-2] == 'A' and \
        grid[row+3][col-3] == 'S':
        return True
    return False

def gridsearch(grid, row, col):
    return searchLeft(grid, row, col) + searchLeftUp(grid,row,col) +\
    searchUp(grid, row, col) + searchRightUp(grid, row, col) +\
    searchRight(grid, row, col) + searchRightDown(grid, row, col) +\
    searchDown(grid, row, col) + searchLeftDown(grid, row, col)


grid = []

with open("day4/input", "r") as fd:
    for line in fd:
        grid.append(line.strip())

count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'X':
            count += gridsearch(grid, i, j)

print("XMAS appears {} times".format(count))