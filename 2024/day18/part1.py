from collections import deque as queue
width = 71
height = 71
# width = 7
# height = 7
end = (height-1,width-1)
start = (0,0)
grid = [["." for i in range(width)] for i in range(height)]
with open("day18/input", "r") as fd:
    count = 0
    for line in fd:
        row, col = line.strip().split(",")
        grid[int(col)][int(row)] = "#"
        count += 1
        if count == 1024:
            break

dRow = [ -1, 0, 1, 0]
dCol = [ 0, 1, 0, -1]

def isValid(vis, row, col):
    if (row < 0 or col < 0 or row >= height or col >= width):
        return False
    if (vis[row][col]):
        return False
    return True
 
def bfs(grid, vis, row, col):
    q = [(row,col)]
    # q.append(( row, col ))
    vis[row][col] = True
    level = 0
    while (len(q) > 0):
        current = []
        for element in q:
            x, y = element[0], element[1]
            if x == end[0] and y == end[1]:
                return level
            for i in range(4):
                adjx = x + dRow[i]
                adjy = y + dCol[i]
                if (isValid(vis, adjx, adjy) and grid[adjx][adjy] == "."):
                    current.append((adjx, adjy))
                    vis[adjx][adjy] = True
        q = current
        level += 1
    return False

vis = [[ False for i in range(width)] for i in range(height)]

shortest_path = bfs(grid, vis, start[0], start[1])
print("length of shortest path from 0,0 to 70,70 is ", shortest_path)
