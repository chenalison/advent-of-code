acost = 3
bcost = 1
error = 10000000000000
eachgroup = []
with open("day13/input", "r") as fd:
    eachgroup = fd.read().split("\n\n")

def calculateMachine(ax,ay,bx,by,px,py):
    B=(py*ax-ay*px)/(-ay*bx+by*ax)
    A=(px-bx*B)/ax
    if B == int(B) and A == int(A):
        return B*bcost+A*acost
    return 0

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
    px = int(prize[0].split("=")[1]) + error
    py = int(prize[1].split("=")[1]) + error
    tokens += calculateMachine(ax,ay,bx,by,px,py)

print("{} tokens".format(tokens))