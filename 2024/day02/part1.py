def isIncrease(report):
    for i in range(len(report)-1):
        cur = int(report[i])
        next = int(report[i+1])
        if next-cur >= 1 and next-cur <= 3:
            continue
        else:
            return False
    return True

def isDecrease(report):
    return isIncrease(report[-1::-1])

count = 0

with open("day02/input", "r") as fd:
    for line in fd:
        report = line.split()
        if isIncrease(report) or isDecrease(report):
            count += 1
        
print("number of safe reports: ", count)
