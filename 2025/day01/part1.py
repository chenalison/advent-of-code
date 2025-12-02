current = 50
count = 0

def calculatePosition(current, direction, distance):
    if direction == 'L':
        current -= distance
    else: # R
        current += distance
    return current % 100
        

with open("day01/input", "r") as fd:
    for line in fd:
        direction = line[0]
        distance = int(line[1:])
        current = calculatePosition(current, direction, distance)
        if current == 0:
            count += 1
        
print("password is", count)