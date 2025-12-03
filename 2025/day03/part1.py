def largestJoltage(bank):
    # two pointers?
    i, j = 0, len(bank) - 1
    left = bank[i]
    right = bank[j]
    leftIndex = i
    # find the biggest left first
    for k in range(len(bank)-1):
        if bank[k] > left:
            left = bank[k]
            leftIndex = k
    for k in range(len(bank)-1, leftIndex, -1):
        if bank[k] > right:
            right = bank[k]
    return int(left + right)

count = 0

with open("day03/input", "r") as fd:
    for line in fd:
        count += largestJoltage(line.strip())

print("total output joltage:", count)            