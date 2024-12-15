# takes a really really long time

from collections import deque as queue

width = 101
height = 103

grid = [[0 for j in range(width)] for i in range(height)]
print(len(grid), len(grid[0]))

robots = []
    
with open("day14/input", "r") as fd:
    for line in fd:
        pos, vel = line.strip().split(" ")
        px, py = pos.split("=")[1].split(",")
        vx, vy = vel.split("=")[1].split(",")
        robots.append({"px": int(px), "py": int(py), "vx": int(vx), "vy": int(vy)})
        # # calculate final position after 100 sec
        # x = (int(px)+seconds*int(vx)) % width
        # y = (int(py)+seconds*int(vy)) % height
        # # print(line, px,py,vx,vy,x,y)
        grid[int(py)][int(px)] += 1

# bfs
dRow = [-1, 0, 1, 0]
dCol = [0, 1, 0, -1]
def isValid(vis, row, col):
    if row < 0 or col < 0 or row >= height or col >= width:
        return False
    if vis[row][col]:
        return False
    return True

def countNeighbors(grid, row, col):
    neighbors = 0
    vis = [[False for i in range(len(grid[0]))] for i in range(len(grid))]
    q = queue()
    q.append((row,col))
    vis[row][col] = True
    while (len(q) > 0):
        x,y = q.popleft()
        neighbors += 1
        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if isValid(vis, adjx, adjy) and grid[adjx][adjy] != 0:
                q.append((adjx, adjy))
                vis[adjx][adjy] = True
    return neighbors

# find the largest cluster
def isTree(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0:
                count = max(countNeighbors(grid, i, j), count)
    if count > 15:
        return True
    return False

# def isTree(grid):
#     count = 0
#     for i in range(len(grid)):
#         if [1]*15 in grid[i]:
#             return True
#     return False

seconds = 0
# while grid[1][width//2] == 0:
while not isTree(grid):
# while seconds<100:
    # print(seconds)
    for row in robots:
        grid[row["py"]][row["px"]] -= 1
        row["px"] = (row["px"]+row["vx"]) % width
        row["py"] = (row["py"]+row["vy"]) % height
        grid[row["py"]][row["px"]] += 1
    seconds += 1

with open("day14/output", "w") as fd:
    for i in range(len(grid)):
        fd.write("".join(str(j) for j in grid[i]) + "\n")


print(seconds, "seconds")

