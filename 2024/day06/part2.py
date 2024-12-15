def getStart(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "^":
                return i,j

def traverse(grid, row, col):
    if grid[row][col] == '^':
        i = row - 1
        while i >= 0 and grid[i][col] != "#":
            if grid[i+1][col] == ".":
                grid[i+1][col] = "|"
            else:
                grid[i+1][col] = "+"
            i -= 1
        if i == -1:
            if grid[i+1][col] == ".":
                grid[i+1][col] = "|"
            else:
                grid[i+1][col] = "+"
            return
        grid[i+1][col] = ">"
        return traverse(grid, i+1, col)
    elif grid[row][col] == ">":
        i = col + 1
        while i < len(grid[0]) and grid[row][i] != "#":
            if grid[row][i-1] == ".":
                grid[row][i-1] = "-" 
            else:
                grid[row][i-1] = "+"
            i += 1
        if i == len(grid[0]):
            if grid[row][i-1] == ".":
                grid[row][i-1] = "-" 
            else:
                grid[row][i-1] = "+"
            return
        grid[row][i-1] = "v"
        return traverse(grid, row, i-1)
    elif grid[row][col] == "v":
        i = row + 1
        while i < len(grid) and grid[i][col] != "#":
            if grid[i-1][col] == ".":
                grid[i-1][col] = "|" 
            else:
                grid[i-1][col] = "+" 
            i += 1
        if i == len(grid):
            if grid[i-1][col] == ".":
                grid[i-1][col] = "|" 
            else:
                grid[i-1][col] = "+"
            return
        grid[i-1][col] = "<"
        return traverse(grid, i-1, col)
    elif grid[row][col] == "<":
        i = col - 1
        while i >= 0 and grid[row][i] != "#":
            if grid[row][i+1] == ".":
                grid[row][i+1] = "-"  
            else:
                grid[row][i+1] = "+"
            i -= 1
        if i == -1:
            if grid[row][i+1] == ".":
                grid[row][i+1] = "-"  
            else:
                grid[row][i+1] = "+"
            return
        grid[row][i+1] = "^"
        return traverse(grid, row, i+1)
    else:
        print("something wrong")


grid = []

with open("day06/sample", "r") as fd:
    for line in fd:
        grid.append(list(line.strip()))

startpos = getStart(grid)

traverse(grid, startpos[0], startpos[1])

for i in range(len(grid)):
    print(''.join(grid[i]))