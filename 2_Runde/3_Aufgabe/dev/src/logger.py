from printer import generate_ascii_display

SSN_CODE = [0b1110111, 0b0010010, 0b1011101, 0b1011011, 0b0111010, 0b1101011, 0b1101111, 0b1010010, 0b1111111, 0b1111011, 0b1111110, 0b0101111, 0b1100101, 0b0011111, 0b1101101, 0b1101100]

def set_bit(bin, pos, val):
    if val:
        bin = bin | (0b1 << pos)
    else:
        bin = bin & ~(0b1 << pos)
    return bin

start_num = [int(x, 16) for x in list("418")]
end_num = [int(x, 16) for x in list("4c2")]
current_num = [SSN_CODE[x] for x in start_num]

DIGITS = len(start_num)

removals = [None] * DIGITS
adds = [None] * DIGITS

for pointer in range(DIGITS):
    start_digit = SSN_CODE[start_num[pointer]]
    end_digit = SSN_CODE[end_num[pointer]]
    mask = start_digit ^ end_digit
    removals[pointer] = start_digit & mask
    adds[pointer] = end_digit & mask

print([bin(x) for x in removals], [bin(x) for x in adds])

def find_next_add(current_digit_pos):
    adds_in_digit = adds[current_digit_pos]
    for j in range(7):
        if adds_in_digit & 0b1:
            # print("add")
            current_num[current_digit_pos] = set_bit(current_num[current_digit_pos], j, 1)
            adds[current_digit_pos] = set_bit(adds[current_digit_pos], j, 0)
            return
        adds_in_digit = adds_in_digit >> 1
    for i, adds_in_digit in enumerate(adds):
        for j in range(7):
            if adds_in_digit & 0b1:
                # print("add")
                current_num[i] = set_bit(current_num[i], j, 1)
                adds[i] = set_bit(adds[i], j, 0)
                return
            adds_in_digit >> 1


generate_ascii_display(current_num[:])

def find_removes():
    for i, removals_in_digit in enumerate(removals): #iterates over the digits removes
        for j in range(7): #iterates over segments in digit
            if removals_in_digit & 0b1:
                # print("rem", bin(removals_in_digit), i)
                current_num[i] = set_bit(current_num[i], j, 0)
                find_next_add(i)
                generate_ascii_display(current_num[:])
            removals_in_digit = removals_in_digit >> 1

find_removes()


