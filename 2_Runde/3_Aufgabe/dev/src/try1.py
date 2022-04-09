def print_ssn(ssn):
    VERTICAL = " │ "
    HORIZONTAL = "───"
    EMPTY = "   "
    def line(bit, replace):
        if bit:
            return replace
        return EMPTY
    first = True
    out = []
    while ssn or first:
        digit = ssn & 0b1111111
        out_digit = ""
        out_digit += EMPTY + line(digit >> 6 & 1, HORIZONTAL) + EMPTY + "\n"
        out_digit += line(digit >> 5 & 1, VERTICAL) + EMPTY + line(digit >> 4 & 1, VERTICAL) + "\n"
        out_digit += EMPTY + line(digit >> 3 & 1, HORIZONTAL) + EMPTY + "\n"
        out_digit += line(digit >> 2 & 1, VERTICAL) + EMPTY + line(digit >> 1 & 1, VERTICAL) + "\n"
        out_digit += EMPTY + line(digit >> 0 & 1, HORIZONTAL) + EMPTY + "\n"
        out.insert(0, out_digit)
        ssn = ssn >> 7
        first = False
    for out_digit in out:
        print(out_digit)



def bin_to_ssn(bin):
    SSD_ENCODE = [0b1110111, 0b0010010, 0b1011101, 0b1011011, 0b0111010, 0b1101011, 0b1101111, 0b1010010, 0b1111111, 0b1111011, 0b1111110, 0b0101111, 0b1100101, 0b0011111, 0b1101101, 0b1101100]
    ssn = 0b0
    i = 0
    while bin or i == 0:
        digit = bin & 0b1111
        ssn = ssn | (SSD_ENCODE[digit] << (7*i))
        bin = bin >> 4
        i += 1
    return ssn



x_hex = "A5"

m = 2



x_bin = int(x_hex, 16)
x_ssn = bin_to_ssn(x_bin)
sticks = x_ssn.bit_count()

n = len(x_hex)
max_bin = 16**n - 1

while True:
    max_ssn = bin_to_ssn(max_bin)
    if max_ssn.bit_count() == sticks and (x_ssn ^ max_ssn).bit_count() / 2 <= m:
        break
    max_bin -= 1

print(hex(max_bin))