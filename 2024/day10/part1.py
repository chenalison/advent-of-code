# multisource bfs
from collections import deque as queue

grid = []
with open("day10/input", "r") as fd:
    for line in fd:
        grid.append(list(line.strip()))

grid = [[int(x) for x in line] for line in grid]

dRow = [-1, 0, 1, 0]
dCol = [0, 1, 0, -1]

def isValid(vis, row, col):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return False
    if vis[row][col]:
        return False
    return True

def scoreTrailhead(grid, vis, row, col):
    q = queue()
    q.append((row,col))
    vis[row][col] = True
    count = 0
    while len(q) > 0:
        x, y = q.popleft()
        if grid[x][y] == 9:
            count += 1
        for i in range(4):
            adjx = x + dRow[i]
            adjy = y + dCol[i]
            if (isValid(vis, adjx, adjy) and grid[x][y] + 1 == grid[adjx][adjy]):
                q.append((adjx, adjy))
                vis[adjx][adjy] = True
    return count

total = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0:
            vis = [[False for i in range(len(grid[0]))] for i in range(len(grid))]
            score = scoreTrailhead(grid, vis, i, j)
            total += score
            # print(i, j, score)

print("sum of trailhead scores: ", total)