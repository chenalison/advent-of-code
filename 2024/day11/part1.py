stones = []

with open("day11/input", "r") as fd:
    stones = fd.read().strip().split()

blinks = 25
for i in range(blinks):
    newstones = []
    for j in stones:
        if int(j) == 0:
            newstones.append(1)
        elif len(str(j)) % 2 == 0:
            mid = len(str(j)) // 2
            first = str(j)[:mid]
            second = str(j)[mid:]
            newstones.append(int(first))
            newstones.append(int(second))
        else:
            newstones.append(2024*int(j))
    stones = newstones

print("{} stones after 25 blinks".format(len(stones)))