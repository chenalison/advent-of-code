# convoluted dp from right to left
def checkDesign(design):
    memo = [False]*len(design)
    if design[-1] in patterns:
        memo[-1] = True
    for i in range(len(design)-2,-1,-1):
        if design[i] in patterns:
            memo[i] = memo[i+1]
        if design[i:] in patterns:
            memo[i] = True
        for j in range(i+1, len(design)):
            if design[i:j] in patterns:
                memo[i] = memo[j] or memo[i]
    return memo[0]

with open("day19/input", "r") as fd:
    patterns = fd.readline().strip().split(", ")
    fd.readline()
    designs = []
    count = 0
    for line in fd:
        if checkDesign(line.strip()):
            count += 1

print(count, "possible designs")