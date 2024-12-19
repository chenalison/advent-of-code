def checkDesign(design):
    memo = [0]*len(design)
    if design[-1] in patterns:
        memo[-1] = 1
    for i in range(len(design)-2,-1,-1):
        if design[i] in patterns:
            memo[i] = memo[i+1]
        if design[i:] in patterns:
            memo[i] += 1
        for j in range(i+2, len(design)):
            if design[i:j] in patterns:
                memo[i] += memo[j]
    return memo[0]

with open("day19/input", "r") as fd:
    patterns = fd.readline().strip().split(", ")
    fd.readline()
    designs = []
    count = 0
    for line in fd:
        count += checkDesign(line.strip())

print(count, "possible designs")