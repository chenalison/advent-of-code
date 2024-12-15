diskmap = ""

with open("day9/input", "r") as fd:
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

pointer1 = 0
pointer2 = len(blocks) - 1

while pointer1 < pointer2:
    if blocks[pointer1] != '.':
        pointer1 += 1
        continue
    if blocks[pointer2] == '.':
        pointer2 -= 1
        continue
    assert(blocks[pointer1] == '.')
    assert(blocks[pointer2] != '.')
    blocks[pointer1] = blocks[pointer2]
    blocks[pointer2] = '.'

total = 0

for i in range(len(blocks)):
    if blocks[i] != '.':
        total += i*blocks[i]

print("filesystem checksum is ", total)
    
