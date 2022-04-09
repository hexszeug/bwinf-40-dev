import ssn_drawer
from ssncode import SSN_CODE

def generate_way_ascii(start_num, end_num):
    start_num = [SSN_CODE[x] for x in start_num]
    current_num = start_num[:]
    end_num = [SSN_CODE[x] for x in end_num]
    masks = [a ^ b for a, b in zip(start_num, end_num)]
    rems = [x & m for x, m in zip(start_num, masks)]
    adds = [x & m for x, m in zip(end_num, masks)]
    print(start_num, current_num, end_num, rems, adds)
    del masks
    way = ssn_drawer.generate_ascii_display(current_num)
    def add_stick_to_digit(digit):
        add = adds[digit] << 1
        for i in range(7):
            add = add >> 1
            if add & 1:
                return digit, i
        return None
    for rem_digit in range(len(current_num)):
        rem = rems[rem_digit] << 1
        for i in range(7):
            rem = rem >> 1
            if rem & 1:
                rem_instr = (rem_digit, i)
                add_instr = add_stick_to_digit(rem_digit)
                if add_instr == None:
                    for add_digit in range(len(current_num) -1, -1, -1):
                        add_instr = add_stick_to_digit(add_digit)
                        if add_instr != None: break
                rems[rem_instr[0]] &= ~(1 << rem_instr[1])
                current_num[rem_instr[0]] &= ~(1 << rem_instr[1])
                adds[add_instr[0]] &= ~(1 << add_instr[1])
                current_num[add_instr[0]] |= 1 << add_instr[1]
                way += "\n" + ssn_drawer.generate_ascii_display(current_num, [add_instr])
    return way

print(generate_way_ascii([int(x, 16) for x in list("418")], [int(x, 16) for x in list("4c2")]))
