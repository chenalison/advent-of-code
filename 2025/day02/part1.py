def isInvalidID(num):
    if len(str(num)) % 2 == 1: # odd length so cannot have repeat
        return False
    n = len(str(num))//2
    return str(num)[:n] == str(num)[n:]

with open("day02/input", "r") as fd:
    line = fd.readline()

ranges = line.split(',')
count = 0
for r in ranges:
    [start, stop] = r.split("-")
    for i in range(int(start), int(stop) + 1):
        if isInvalidID(i):
            count += i

print("sum of invalid IDs: ", count)