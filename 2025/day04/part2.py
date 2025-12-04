def countRolls(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                count += 1
    return count

def isValid(grid, i, j):
    return i < len(grid) and i >= 0 and j < len(grid[0]) and j >= 0

def canAccess(grid, i, j):
    count = 0
    if isValid(grid, i-1, j-1) and grid[i-1][j-1] == "@":
        count += 1
    if isValid(grid, i-1, j) and grid[i-1][j] == "@":
        count += 1
    if isValid(grid, i-1, j+1) and grid[i-1][j+1] == "@":
        count += 1
    if isValid(grid, i, j-1) and grid[i][j-1] == "@":
        count += 1
    if isValid(grid, i, j+1) and grid[i][j+1] == "@":
        count += 1
    if isValid(grid, i+1, j-1) and grid[i+1][j-1] == "@":
        count += 1
    if isValid(grid, i+1, j) and grid[i+1][j] == "@":
        count += 1
    if isValid(grid, i+1, j+1) and grid[i+1][j+1] == "@":
        count += 1        
    return count < 4

def removeRolls(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@" and canAccess(grid, i, j):
                grid[i][j] = "."
    return grid

grid = []

with open("day04/input", "r") as fd:
    for line in fd:
        grid.append(list(line.strip()))

start = countRolls(grid)

while True:
    before = countRolls(grid)
    grid = removeRolls(grid)
    after = countRolls(grid)
    if after == before:
        break

end = countRolls(grid)

print("total rolls of paper removed:", start - end)