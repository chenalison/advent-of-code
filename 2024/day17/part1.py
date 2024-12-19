with open("day17/input", "r") as fd:
    regA = int(fd.readline().split(":")[1].strip())
    regB = int(fd.readline().split(":")[1].strip())
    regC = int(fd.readline().split(":")[1].strip())
    fd.readline() # empty
    program = fd.readline().split(":")[1].strip().split(",")
# opcode,operand,opcode,operand
def combo(num):
    if num in ["0", "1", "2", "3"]:
        return int(num)
    elif num == "4":
        return regA
    elif num == "5":
        return regB
    elif num == "6":
        return regC
    # else 7
def adv(operand):
    denom = 2**combo(operand)
    return int(regA / denom)
def bxl(operand):
    return regB ^ int(operand)
def bst(operand):
    return combo(operand) % 8
def bxc(operand):
    return regB ^ regC
ptr = 0
output = []
while ptr < len(program):
    # print(ptr)
    if program[ptr] == "0":
        regA = adv(program[ptr+1])
    elif program[ptr] == "1":
        regB = bxl(program[ptr+1])
    elif program[ptr] == "2":
        regB = bst(program[ptr+1])
    elif program[ptr] == "3":
        if regA != 0:
            ptr = int(program[ptr+1])
            continue
    elif program[ptr] == "4":
        regB = bxc(program[ptr+1])
    elif program[ptr] == "5":
        output.append(bst(program[ptr+1]))
    elif program[ptr] == "6":
        regB = adv(program[ptr+1])
    elif program[ptr] == "7":
        regC = adv(program[ptr+1])
    ptr += 2

str_output = [str(x) for x in output]
print("output ", ",".join(str_output))