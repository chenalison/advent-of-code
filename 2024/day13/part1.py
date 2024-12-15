# overthought dp and took too long
acost = 3
bcost = 1
times = 100
eachgroup = []
with open("day13/input", "r") as fd:
    eachgroup = fd.read().split("\n\n")

def calculateMachine(ax,ay,bx,by,px,py):
    possible = []
    # memox = [[float('inf') for i in range(times)] for i in range(times)]
    # memoy = [[float('inf') for i in range(times)] for i in range(times)]
    for i in range(times):
        for j in range(times):
            # memox[i][j] = ax*i+bx*j
            # memoy[i][j] = ay*i+by*j
            # if memox[i][j] == px and memoy[i][j] == py:
            if ax*i+bx*j == px and ay*i+by*j == py:
                possible.append([i,j])
    if len(possible) == 0:
        return 0
    tokens = float('inf')
    for i,j in possible:
        tokens = min(tokens, i*acost+j*bcost)
    return tokens

tokens = 0
for txt in eachgroup:
    lines = txt.split('\n')
    # A
    a = lines[0].split(": ")[1].split(", ")
    ax = int(a[0].split("+")[1])
    ay = int(a[1].split("+")[1])
    # B
    b = lines[1].split(": ")[1].split(", ")
    bx = int(b[0].split("+")[1])
    by = int(b[1].split("+")[1])
    # prize
    prize = lines[2].split(": ")[1].split(", ")
    px = int(prize[0].split("=")[1])
    py = int(prize[1].split("=")[1])
    # print(lines)
    # print(ax,ay,bx,by,px,py)
    tokens += calculateMachine(ax,ay,bx,by,px,py)

print("{} tokens".format(tokens))