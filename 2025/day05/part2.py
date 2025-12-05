def sumIntervals(intervals):
    count = 0
    for start, end in intervals:
        count += end - start + 1
    return count

def combineIntervals(intervals):
    i = 0
    while i + 1 < len(intervals):
        start1, end1 = intervals[i]
        start2, end2 = intervals[i+1]
        if start2 >= start1 and start2 <= end1:
            if end1 > end2:
                intervals[i] = (start1, end1)
            else:
                intervals[i] = (start1, end2)
            del intervals[i+1]
        else:
            i += 1
    return intervals

count = 0
fresh = []

with open("day05/input", "r") as fd:
    ranges, _ = fd.read().split("\n\n")
    for txt in ranges.split("\n"):
        start, end = txt.strip().split('-')
        fresh.append((int(start), int(end)))

fresh.sort()
fresh = combineIntervals(fresh)
    
print("number of fresh IDs:", sumIntervals(fresh))