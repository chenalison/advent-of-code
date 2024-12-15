import re

instructions = ""

with open("day03/input", "r") as fd:
    for line in fd:
        instructions += line

results = 0

mul = re.findall("mul\([0-9]+,[0-9]+\)", instructions)

for i in mul:
    idx = i.find(",")
    first = i[4:idx]
    second = i[idx+1:-1]
    results += int(first) * int(second)

print("Result: ", results)