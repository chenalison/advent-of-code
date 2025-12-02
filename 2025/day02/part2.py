def isInvalidID(num):
    n = len(str(num))
    for i in range(1, n//2+1):
        if n/i != n//i:
            pass # not possible repeat
        times = n//i
        segment = str(num)[:i]
        if segment*times == str(num):
            return True
    return False

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