# takes a long time

diskmap = ""

with open("day09/input", "r") as fd:
    diskmap = fd.read().strip()

id = 0
blocks = []
for i in range(len(diskmap)):
    if i % 2 == 0: # file
        for i in range(int(diskmap[i])):
            blocks.append(id)
        id += 1
    else: # free space
        for i in range(int(diskmap[i])):
            blocks.append('.')
# print(blocks)

pointer1 = 0
pointer2 = len(blocks) - 1
lastID = float('inf')
while pointer1 < pointer2:
    # print(pointer1, pointer2)
    if blocks[pointer1] != '.':
        pointer1 += 1
        continue
    if blocks[pointer2] == '.':
        pointer2 -= 1
        continue
    if blocks[pointer2] > lastID:
        pointer2 -= 1
        continue
    assert(blocks[pointer1] == '.')
    assert(blocks[pointer2] != '.')
    moveID = blocks[pointer2]
    movelen = 1
    while blocks[pointer2-movelen] == moveID:
        movelen += 1
    # print("pointer2", moveID, movelen)
    newloc = pointer1
    targetlen = 0
    for i in range(pointer1, pointer2):
        if blocks[i] == ".":
            targetlen += 1
            if targetlen >= movelen:
                break
        else:
            newloc = i + 1
            targetlen = 0
    if targetlen >= movelen:
        # print("moved starting from", newloc, "and", pointer2)
        for i in range(movelen):
            blocks[newloc+i] = moveID
            blocks[pointer2-i] = '.'
    else:
        pointer2 -= movelen
    lastID = moveID

total = 0

for i in range(len(blocks)):
    if blocks[i] != '.':
        total += i*blocks[i]
# print(blocks)
print("filesystem checksum is ", total)
    
