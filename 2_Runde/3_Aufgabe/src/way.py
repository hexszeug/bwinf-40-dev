import ssn_drawer
import ascii_box
from ssncode import SSN_CODE

def generate_way_ascii(start_num, end_num, max_line_width = 70):
    #prepare variables
    start_num = [SSN_CODE[x] for x in start_num]
    current_num = start_num[:]
    end_num = [SSN_CODE[x] for x in end_num]
    masks = [a ^ b for a, b in zip(start_num, end_num)]
    rems = [x & m for x, m in zip(start_num, masks)]
    adds = [x & m for x, m in zip(end_num, masks)]
    del masks
    #print start number
    way = ssn_drawer.generate_ascii_display(current_num, max_width=max_line_width)
    #calculate way
    def add_stick_to_digit(digit):
        add = adds[digit] << 1
        for i in range(7):
            add = add >> 1
            if add & 1:
                return digit, i
        return None#
    for rem_digit in range(len(current_num)): #iterates over digits in rems
        rem = rems[rem_digit] << 1
        for i in range(7): #iterates over segments in current digit
            rem = rem >> 1
            if rem & 1: #segment is turned on -> has to turn off
                rem_instr = (rem_digit, i)
                add_instr = add_stick_to_digit(rem_digit) #try turn different segment in same digit on
                if add_instr == None: #no segment in same digit has to turn on -> search in other digits
                    for add_digit in range(len(current_num)):
                        add_instr = add_stick_to_digit(add_digit)
                        if add_instr != None: break
                rems[rem_instr[0]] &= ~(1 << rem_instr[1]) #turn off segment in rems
                current_num[rem_instr[0]] &= ~(1 << rem_instr[1]) #turn off segment in current num
                adds[add_instr[0]] &= ~(1 << add_instr[1]) #turn off segment in adds
                current_num[add_instr[0]] |= 1 << add_instr[1] #turn on segment in current num
                way += f"\n{ascii_box.generate_pixel([0, 2, 0, 2]) * max_line_width}{ssn_drawer.generate_ascii_display(current_num, [add_instr], max_line_width)}"
    return way

# print(generate_way_ascii([int(x, 16) for x in list("73fe7d782")], [int(x, 16) for x in list("fffffd782")]))
