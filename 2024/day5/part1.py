from collections import defaultdict

with open("day5/input", "r") as fd:
    rules, updates = fd.read().split('\n\n')
    rules = rules.split()
    updates = updates.split()

rulesDict = defaultdict(set)
for i in rules:
    i = i.strip()
    first, second = i.split("|")
    rulesDict[first].add(second)

def checkOrder(pages, rulesDict):
    for j in range(len(pages)):
        for k in range(j+1, len(pages)):
            if pages[j] in rulesDict[pages[k]]:
                return False
    return True

count = 0

for i in updates:
    pages = i.strip().split(",")
    if checkOrder(pages, rulesDict):
        count += int(pages[len(pages)//2])

print("Sum of correctly ordered middle pages: ", count)
    

