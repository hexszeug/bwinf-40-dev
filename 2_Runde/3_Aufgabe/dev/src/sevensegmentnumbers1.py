SSN_CODEC = [0b1110111, 0b0010010, 0b1011101, 0b1011011, 0b0111010, 0b1101011, 0b1101111, 0b1010010, 0b1111111, 0b1111011, 0b1111110, 0b0101111, 0b1100101, 0b0011111, 0b1101101, 0b1101100]

def convert(digit):
    return SSN_CODEC[digit]

# def bin_to_ssn(bin):
#     ssn = 0b0
#     i = 0
#     while bin or i == 0:
#         digit = bin & 0b1111
#         ssn = ssn | (bin_digit_to_ssn(digit) << (7*i))
#         bin = bin >> 4
#         i += 1
#     return ssn