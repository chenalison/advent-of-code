with open("day15/input", "r") as fd:
    lines = fd.read().split('\n\n')
    instructions = "".join(lines[1].strip().split("\n"))
    grid = []
    for line in lines[0].split('\n'):
        grid.append(list(line))

def findStart(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                return i,j

def moveUp(grid):
    row, col = findStart(grid)
    if row - 1 < 0:
        return
    if grid[row-1][col] == "#":
        return
    elif grid[row-1][col] == ".":
        grid[row][col] = "."
        grid[row-1][col] = "@"
    elif grid[row-1][col] == "O":
        # look for first . after O
        curr = row-1
        while curr > 0 and grid[curr][col] == "O":
            curr -= 1
        if grid[curr][col] == ".":
            grid[curr][col] = "O"
            grid[row][col] = "."
            grid[row-1][col] = "@"
        # else do nothing

def moveRight(grid):
    row, col = findStart(grid)
    if col+1 >= len(grid[0]):
        return
    if grid[row][col+1] == "#":
        return
    elif grid[row][col+1] == ".":
        grid[row][col] = "."
        grid[row][col+1] = "@"
    elif grid[row][col+1] == "O":
        # look for first . after O
        curr = col+1
        while curr < len(grid[0]) and grid[row][curr] == "O":
            curr += 1
        if grid[row][curr] == ".":
            grid[row][curr] = "O"
            grid[row][col] = "."
            grid[row][col+1] = "@"
        # else do nothing
    
def moveDown(grid):
    row, col = findStart(grid)
    if row + 1 >= len(grid):
        return
    if grid[row+1][col] == "#":
        return
    elif grid[row+1][col] == ".":
        grid[row][col] = "."
        grid[row+1][col] = "@"
    elif grid[row+1][col] == "O":
        # look for first . after O
        curr = row+1
        while curr < len(grid) and grid[curr][col] == "O":
            curr += 1
        if grid[curr][col] == ".":
            grid[curr][col] = "O"
            grid[row][col] = "."
            grid[row+1][col] = "@"
        # else do nothing

def moveLeft(grid):
    row, col = findStart(grid)
    if col-1 < 0:
        return
    if grid[row][col-1] == "#":
        return
    elif grid[row][col-1] == ".":
        grid[row][col] = "."
        grid[row][col-1] = "@"
    elif grid[row][col-1] == "O":
        # look for first . after O
        curr = col-1
        while curr > 0 and grid[row][curr] == "O":
            curr -= 1
        if grid[row][curr] == ".":
            grid[row][curr] = "O"
            grid[row][col] = "."
            grid[row][col-1] = "@"
        # else do nothing

def applyMove(grid, dir):
    if dir == '^':
        moveUp(grid)
    elif dir == '>':
        moveRight(grid)
    elif dir == 'v':
        moveDown(grid)
    elif dir == '<':
        moveLeft(grid)

for i in instructions:
    applyMove(grid, i)




def calcCoords(grid):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "O":
                total += 100 * i + j
    return total

# for i in range(len(grid)):
#     print("".join(grid[i]))
    
total = calcCoords(grid)
print("sum of all boxes' GPS coords: ", total)
