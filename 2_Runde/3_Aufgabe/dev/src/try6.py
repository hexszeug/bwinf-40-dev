SSN_CODE = [0b1110111, 0b0010010, 0b1011101, 0b1011011, 0b0111010, 0b1101011, 0b1101111, 0b1010010, 0b1111111, 0b1111011, 0b1111110, 0b0101111, 0b1100101, 0b0011111, 0b1101101, 0b1101100]

BASE = len(SSN_CODE)

input_string = "73fe7d782"

INITIAL_NUM = [int(x, BASE) for x in list(input_string)]
MAX_MOVES = 8
DIGITS = len(INITIAL_NUM)

ssn_code_number_of_sticks = [x.bit_count() for x in SSN_CODE]
max_sticks = max(ssn_code_number_of_sticks)
min_sticks = min(ssn_code_number_of_sticks)
balance_max_limit = [0]
balance_min_limit = [0]
rev_num = INITIAL_NUM[:]
rev_num.reverse()
for digit in rev_num:
    balance_max_limit.insert(0, max_sticks - SSN_CODE[digit].bit_count() + balance_max_limit[0])
    balance_min_limit.insert(0, min_sticks - SSN_CODE[digit].bit_count() + balance_min_limit[0])
balance_max_limit.pop(0)
balance_min_limit.pop(0)

del ssn_code_number_of_sticks, max_sticks, min_sticks, rev_num


optimized_num = [0x10] * DIGITS
moves_digitwise = [0] * DIGITS
balance_digitwise = [0] * DIGITS
pointer = DIGITS


def optimize_variant_1(pointer, prefered_digit):
    moves_left = MAX_MOVES - sum(moves_digitwise[:-pointer-1])
    balance = sum(balance_digitwise[:-pointer-1])
    initial_digit = INITIAL_NUM[-pointer-1]
    initial_digit_ssn = SSN_CODE[initial_digit]
    for optimized_digit in range(prefered_digit, -1, -1):
        optimized_digit_ssn = SSN_CODE[optimized_digit]
        mask = initial_digit_ssn ^ optimized_digit_ssn
        remove_sticks = (initial_digit_ssn & mask).bit_count()
        add_sticks = (optimized_digit_ssn & mask).bit_count()
        new_balance = balance
        moves = 0
        moves += max(min(new_balance, 0) + remove_sticks, 0)
        new_balance += remove_sticks
        moves += max(min(-new_balance, 0) + add_sticks, 0)
        new_balance -= add_sticks
        #VALIDATE
        if moves > moves_left: continue
        if new_balance > balance_max_limit[-pointer-1] or new_balance < balance_min_limit[-pointer-1]: continue
        optimized_num[-pointer-1] = optimized_digit
        moves_digitwise[-pointer-1] = moves
        balance_digitwise[-pointer-1] = new_balance - balance
        return True
    return False

while pointer > 0:
    pointer -= 1
    if not optimize_variant_1(pointer, optimized_num[-pointer-1] - 1):
        pointer += 2


# print(INITIAL_NUM)
print(optimized_num)
print(sum(balance_digitwise))
print(sum(moves_digitwise))