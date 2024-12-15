
def getStart(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                return i,j

def countX(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "X":
                count += 1
    return count

def traverse(grid, row, col):
    if grid[row][col] == '^':
        i = row - 1
        while i >= 0 and grid[i][col] != "#":
            grid[i+1][col] = "X"
            i -= 1
        if i == -1:
            grid[i+1][col] == "X"
            return
        grid[i+1][col] = ">"
        return traverse(grid, i+1, col)
    elif grid[row][col] == ">":
        i = col + 1
        while i < len(grid[0]) and grid[row][i] != "#":
            grid[row][i-1] = "X"
            i += 1
        if i == len(grid[0]):
            grid[row][i-1] = "X"
            return
        grid[row][i-1] = "v"
        return traverse(grid, row, i-1)
    elif grid[row][col] == "v":
        i = row + 1
        while i < len(grid) and grid[i][col] != "#":
            grid[i-1][col] = "X"
            i += 1
        if i == len(grid):
            grid[i-1][col] = "X"
            return
        grid[i-1][col] = "<"
        return traverse(grid, i-1, col)
    elif grid[row][col] == "<":
        i = col - 1
        while i >= 0 and grid[row][i] != "#":
            grid[row][i+1] = "X"
            i -= 1
        if i == -1:
            grid[row][i+1] = "X"
            return
        grid[row][i+1] = "^"
        return traverse(grid, row, i+1)
    else:
        print("something wrong")


grid = []

with open("day6/input", "r") as fd:
    for line in fd:
        grid.append(list(line.strip()))

startpos = getStart(grid)

traverse(grid, startpos[0], startpos[1])

pos = countX(grid)

print("{} distinct positions".format(pos))