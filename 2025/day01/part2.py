current = 50
count = 0

def calculatePosition(current, direction, distance):
    if direction == 'L':
        current -= distance
        # trial and error lol
        additional = 0
        if current <= 0 and current + distance > 0:
            additional = 1
        additional += abs(current) // 100
    else: # R
        current += distance
        additional = current // 100
    return current % 100, additional
        

with open("day01/input", "r") as fd:
    for line in fd:
        direction = line[0]
        distance = int(line[1:])
        current, additional = calculatePosition(current, direction, distance)
        count += additional
        
print("password is", count)