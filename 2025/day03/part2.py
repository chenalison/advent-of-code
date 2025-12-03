# find the biggest number from the left until len - 12
# then from prev start until len - 11
# continue until you found 12
# if the remaining to search == number you still need then add all the rest

def largestJoltage(bank):
    remaining = 12
    current = ""
    leftIndex = 0
    while len(current) < remaining:
        if len(bank[leftIndex:]) == remaining - len(current):
            current += bank[leftIndex:]
            break
        left = bank[leftIndex]
        for k in range(leftIndex, len(bank) - remaining + 1 + len(current)):
            if bank[k] > left:
                left = bank[k]
                leftIndex = k
        current += left
        leftIndex += 1
    return int(current)

count = 0

with open("day03/input", "r") as fd:
    for line in fd:
        count += largestJoltage(line.strip())

print("total output joltage:", count)