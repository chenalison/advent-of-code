from collections import defaultdict

rcount = defaultdict(int)
left = []
with open("day01/input", "r") as fd:
    for line in fd:
        left.append(int(line.split()[0]))
        rcount[int(line.split()[1])] += 1

sim = 0
for i in left:
    sim += rcount[i] * i

print("Simiarity Score:", sim)