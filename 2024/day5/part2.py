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

def reOrder(pages, rulesDict):
    for j in range(len(pages)):
        for k in range(j+1, len(pages)):
            if pages[j] in rulesDict[pages[k]]:
                newpages = pages
                temp = newpages[j]
                newpages[j] = newpages[k]
                newpages[k]= temp
                return reOrder(newpages, rulesDict)
    return pages


count = 0

for i in updates:
    pages = i.strip().split(",")
    if not checkOrder(pages, rulesDict):
        newOrder = reOrder(pages, rulesDict)
        count += int(pages[len(pages)//2])

print("Sum of incorrectly ordered middle pages: ", count)