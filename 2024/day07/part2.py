def evaluateEq(target, numlist):
    results = [int(numlist[0])]
    for i in range(1,len(numlist)):
        newresults = []
        for j in results:
            newresults.append(j+int(numlist[i]))
            newresults.append(j*int(numlist[i]))
            newresults.append(int(str(j) + numlist[i]))
        results = newresults
    if target in results:
        return True
    return False

lines = []
count = 0

with open("day07/input", "r") as fd:
    for line in fd:
        target, numbers = line.split(":")
        numlist = numbers.split()
        if evaluateEq(int(target), numlist):
            count += int(target)

print("Total calibration result: ", count)