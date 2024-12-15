from collections import defaultdict

stones = []

with open("day11/input", "r") as fd:
    stones = fd.read().strip().split()

stones = [int(item) for item in stones]
stonesFreq = {key: 1 for key in stones}

blinks = 75
for i in range(blinks):
    newstones = defaultdict(int)
    for k,v in stonesFreq.items():
        if int(k) == 0:
            newstones[1] += v
        elif len(str(k)) % 2 == 0:
            mid = len(str(k)) // 2
            first = str(k)[:mid]
            second = str(k)[mid:]
            newstones[int(first)] += v
            newstones[int(second)] += v
        else:
            newstones[2024*int(k)] += v
    stonesFreq = newstones
total = 0
for k,v in stonesFreq.items():
    total += v
print("{} stones after 25 blinks".format(total))