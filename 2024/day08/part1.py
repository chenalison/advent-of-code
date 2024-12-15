empty = []
grid = []

with open("day08/input", "r") as fd:
    for line in fd:
        grid.append(list(line.strip()))
        empty.append(list('.'*len(line.strip())))

antennas = set()

for i in grid:
    for j in i:
        if j != '.':
            antennas.add(j)

def placeAntinode(empty, grid, antenna):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == antenna:
                # print(i,j)
                for k in range(i, len(grid)):
                    for l in range(0, len(grid[0])):
                        if k == i and l == j:
                            continue
                        if grid[k][l] == antenna:
                            # distance
                            vertical = k - i
                            horizontal = l - j
                            # print(i,j,k,l,vertical,horizontal,k+vertical,l+horizontal,i-vertical,j-horizontal)
                            if k+vertical < len(grid) and k+vertical >= 0 and l+horizontal < len(grid[0]) and l+horizontal >= 0:
                                empty[k+vertical][l+horizontal] = "#"
                            if i-vertical >= 0 and i-vertical < len(grid) and j-horizontal >= 0 and j-horizontal < len(grid[0]):
                                empty[i-vertical][j-horizontal] = "#"
for i in antennas:
    placeAntinode(empty, grid, i)

def countAntinodes(empty):
    count = 0
    for i in empty:
        for j in i:
            if j == '#':
                count += 1
    return count

count = countAntinodes(empty)

print(count, " antinodes")