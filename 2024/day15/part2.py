# spent forever figuring out/debugging push up and down
with open("day15/input", "r") as fd:
    lines = fd.read().split('\n\n')
    instructions = "".join(lines[1].strip().split("\n"))
    grid = []
    for line in lines[0].split('\n'):
        grid.append(list(line))

def printGrid(grid):
    for i in range(len(grid)):
        print("".join(grid[i]))

# convert grid
newGrid = []
for i in range(len(grid)):
    newRow = []
    for j in range(len(grid[0])):
        if grid[i][j] == "#":
            newRow.append("#")
            newRow.append("#")
        elif grid[i][j] == "O":
            newRow.append("[")
            newRow.append("]")
        elif grid[i][j] == ".":
            newRow.append(".")
            newRow.append(".")
        elif grid[i][j] == "@":
            newRow.append("@")
            newRow.append(".")
    newGrid.append(newRow)

# printGrid(newGrid)

def findStart(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "@":
                return i,j
            
def pushDown(grid, row, col):
    if grid[row+1][col] == "#" or grid[row+1][col+1] == "#":
        return False
    if grid[row+1][col] == "." and grid[row+1][col+1] == ".":
        return True
    if grid[row+1][col] == "[":
        return pushDown(grid, row+1, col)
    if grid[row+1][col] == "]" and grid[row+1][col+1] == "[":
        return pushDown(grid, row+1, col-1) and pushDown(grid, row+1, col+1)
    if grid[row+1][col] == "]" and grid[row+1][col+1] == ".":
        return pushDown(grid, row+1, col-1)
    if grid[row+1][col+1] == "[" and grid[row+1][col] == ".":
        return pushDown(grid, row+1, col+1)
    
def pushUp(grid, row, col): # row, col is where [ is
    if grid[row-1][col] == "#" or grid[row-1][col+1] == "#":
        return False
    if grid[row-1][col] == "." and grid[row-1][col+1] == ".":
        return True
    if grid[row-1][col] == "[":
        return pushUp(grid, row-1, col)
    if grid[row-1][col] == "]" and grid[row-1][col+1] == "[":
        return pushUp(grid, row-1, col-1) and pushUp(grid, row-1, col+1)
    if grid[row-1][col] == "]" and grid[row-1][col+1] == ".":
        return pushUp(grid, row-1, col-1)
    if grid[row-1][col] == "." and grid[row-1][col+1] == "[":
        return pushUp(grid, row-1, col+1)
    
def updatePushDown(grid, row, col):
    # print(row, col)
    if grid[row][col] == "]":
        updatePushDown(grid, row+1, col-1)
        grid[row][col-1] = "."
    if grid[row][col] == "[":
        updatePushDown(grid, row+1, col)
    if grid[row][col+1] == "[":
        updatePushDown(grid, row+1, col+1)
        grid[row][col+2] = "."
    grid[row][col] = "["
    grid[row][col+1] = "]"

def updatePushUp(grid, row, col): # row, col is where [ is located
    # print(row, col)
    if grid[row][col] == "]":
        updatePushUp(grid, row-1, col-1)
        grid[row][col-1] = "."
    if grid[row][col] == "[":
        updatePushUp(grid, row-1, col)
    if grid[row][col+1] == "[":
        updatePushUp(grid, row-1, col+1)
        grid[row][col+2] = "."
    grid[row][col] = "["
    grid[row][col+1] = "]"

def moveUp(grid):
    row, col = findStart(grid)
    if row - 1 < 0:
        return
    if grid[row-1][col] == "#":
        return
    elif grid[row-1][col] == ".":
        grid[row][col] = "."
        grid[row-1][col] = "@"
    elif grid[row-1][col] == "]":
        if pushUp(grid, row-1, col-1):
            updatePushUp(grid, row-2, col-1)
            grid[row-1][col] = "@"
            grid[row-1][col-1] = "."
            grid[row][col] = "."
    elif grid[row-1][col] == "[":
        if pushUp(grid, row-1, col):
            updatePushUp(grid, row-2, col)
            grid[row-1][col] = "@"
            grid[row-1][col+1] = "."
            grid[row][col] = "."

def moveRight(grid):
    row, col = findStart(grid)
    if col+1 >= len(grid[0]):
        return
    if grid[row][col+1] == "#":
        return
    elif grid[row][col+1] == ".":
        grid[row][col] = "."
        grid[row][col+1] = "@"
    elif grid[row][col+1] == "[":
        curr = col+1
        while curr < len(grid[0]) and grid[row][curr] == "[":
            curr += 2
        if grid[row][curr] == ".":
            for i in range(col+2, curr, 2):
                grid[row][i] = "["
                grid[row][i+1] = "]"
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
    elif grid[row+1][col] == "]":
        if pushDown(grid, row+1, col-1):
            updatePushDown(grid, row+2, col-1)
            grid[row+1][col] = "@"
            grid[row+1][col-1] = "."
            grid[row][col] = "."
    elif grid[row+1][col] == "[":
        if pushDown(grid, row+1, col):
            updatePushDown(grid, row+2, col)
            grid[row+1][col] = "@"
            grid[row+1][col+1] = "."
            grid[row][col] = "."

def moveLeft(grid):
    row, col = findStart(grid)
    if col-1 < 0:
        return
    if grid[row][col-1] == "#":
        return
    elif grid[row][col-1] == ".":
        grid[row][col] = "."
        grid[row][col-1] = "@"
    elif grid[row][col-1] == "]":
        curr = col-1
        while curr > 0 and grid[row][curr] == "]":
            curr -= 2
        if grid[row][curr] == ".":
            for i in range(col-2, curr, -2):
                grid[row][i] = "]"
                grid[row][i-1] = "["
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

def countSquares(newGrid):
    count = 0
    for i in range(len(newGrid)):
        for j in range(len(newGrid[0])):
            if newGrid[i][j] == '[':
                count += 1
    return count

def completeSquares(newGrid):
    countL = 0
    countR = 0
    for i in range(len(newGrid)):
        for j in range(len(newGrid[0])):
            if newGrid[i][j] == '[':
                countL += 1
            elif newGrid[i][j] == "]":
                countR += 1
    return countL == countR

for i in instructions:
    # print("move", i)
    applyMove(newGrid, i)
    # printGrid(newGrid)
    assert(completeSquares(newGrid))
    # assert(countSquares(newGrid) == 21)



def calcCoords(grid):
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "[":
                total += 100 * i + j
    return total

# printGrid(newGrid)

total = calcCoords(newGrid)
print("sum of all boxes' GPS coords: ", total)