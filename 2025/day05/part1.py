count = 0
fresh = []

with open("day05/input", "r") as fd:
    ranges, available = fd.read().split("\n\n")
    for txt in ranges.split("\n"):
        start, end = txt.strip().split('-')
        fresh.append((int(start), int(end)))
    
    for txt in available.split("\n"):
        txt = int(txt)
        for start, end in fresh:
            if txt > start and txt < end:
                count += 1
                break

print("number of fresh ingredients:", count)
