
width = 101
height = 103
# width = 11
# height = 7
seconds = 100

grid = [[0 for j in range(width)] for i in range(height)]
print(len(grid), len(grid[0]))
    
with open("day14/input", "r") as fd:
    for line in fd:
        pos, vel = line.strip().split(" ")
        px, py = pos.split("=")[1].split(",")
        vx, vy = vel.split("=")[1].split(",")
        # calculate final position after 100 sec
        x = (int(px)+seconds*int(vx)) % width
        y = (int(py)+seconds*int(vy)) % height
        # print(line, px,py,vx,vy,x,y)
        grid[y][x] += 1
        

def countRobots(grid):
    counts = [0,0,0,0]
    for i in range(height//2):
        for j in range(width//2):
            counts[0] += grid[i][j]
        for j in range(width//2+1, width):
            counts[1] += grid[i][j]
    for i in range(height//2 + 1, height):
        for j in range(width//2):
            counts[2] += grid[i][j]
        for j in range(width//2+1, width):
            counts[3] += grid[i][j]
    result = 1
    # print(counts)
    for i in counts:
        result *= i
    return result

# for i in range(len(grid)):
#     print("".join(str(j) for j in grid[i]))
total = countRobots(grid)

print("safety factor: ", total)