

def removeLevel(report, idx):
    newreport = report[:idx] + report[idx+1:]
    return isIncrease(newreport, True)

def isIncrease(report, removedLevel = False):
    for i in range(len(report)-1):
        cur = int(report[i])
        next = int(report[i+1])
        if next-cur >= 1 and next-cur <= 3:
            continue
        elif removedLevel:
            return False
        else:
            return removeLevel(report, i) or removeLevel(report, i+1)
    return True

def isDecrease(report):
    return isIncrease(report[-1::-1])

count = 0

with open("day2/input", "r") as fd:
    for line in fd:
        report = line.split()
        if isIncrease(report) or isDecrease(report):
            count += 1
        
print("number of safe reports: ", count)
