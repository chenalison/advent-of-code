import heapq
import math

left = []
right = []

with open("day01/input", "r") as fd:
    for line in fd:
        left.append(int(line.split()[0]))
        right.append(int(line.split()[1]))

heapq.heapify(left)
heapq.heapify(right)

total = 0

for i in range(len(left)):
    leftv = heapq.heappop(left)
    rightv = heapq.heappop(right)
    total += abs(leftv - rightv)

print("Total difference: ", total)
        