import re

instructions = ""

with open("day03/input", "r") as fd:
    for line in fd:
        instructions += line

keepInstructions = ""
enable = True
i = 0
while i < len(instructions):
    if enable:
        idx = instructions.find("don't()", i)
        if idx == -1:
            keepInstructions += instructions[i:]
            break
        keepInstructions += instructions[i:idx]
        enable = False
        i = idx + 6
    else:
        idx = instructions.find("do()", i)
        if idx == -1:
            break
        enable = True
        i = idx + 3

results = 0

mul = re.findall("mul\([0-9]+,[0-9]+\)", keepInstructions)

for i in mul:
    idx = i.find(",")
    first = i[4:idx]
    second = i[idx+1:-1]
    results += int(first) * int(second)

print("Result: ", results)