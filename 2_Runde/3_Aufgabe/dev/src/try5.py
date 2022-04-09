SSN_CODE = [0b1110111, 0b0010010, 0b1011101, 0b1011011, 0b0111010, 0b1101011, 0b1101111, 0b1010010, 0b1111111, 0b1111011, 0b1111110, 0b0101111, 0b1100101, 0b0011111, 0b1101101, 0b1101100]

BASE = len(SSN_CODE)

input_string = "5A10"

INITIAL_NUM = [int(x, BASE) for x in list(input_string)]
MAX_MOVES = 200000
DIGITS = len(INITIAL_NUM)


ssn_code_number_of_sticks = [x.bit_count() for x in SSN_CODE]
max_sticks = max(ssn_code_number_of_sticks)
min_sticks = min(ssn_code_number_of_sticks)

possible_balance_decrease_digitwise = [0]
possible_balance_increase_digitwise = [0]

rev_num = INITIAL_NUM[:]
rev_num.reverse()

for digit in rev_num:
    possible_balance_decrease_digitwise.insert(0, abs(SSN_CODE[digit].bit_count() - max_sticks) + possible_balance_decrease_digitwise[0])
    possible_balance_increase_digitwise.insert(0, abs(SSN_CODE[digit].bit_count() - min_sticks) + possible_balance_increase_digitwise[0])

possible_balance_decrease_digitwise.pop(-1)
possible_balance_increase_digitwise.pop(-1)


optimized_num = INITIAL_NUM[:]
moves_digitwise = [0] * DIGITS
balance_digitwise = [0] * DIGITS
pointer = DIGITS


def optimize_digit(pointer, preferred_digit):
    initial_digit = INITIAL_NUM[-pointer-1]
    moves_left = MAX_MOVES - sum(moves_digitwise[:-pointer-1])
    balance = sum(balance_digitwise[:-pointer-1])
    initial_digit_ssn = SSN_CODE[initial_digit]
    for optimized_digit in range(preferred_digit, -1, -1):
        if optimized_digit == initial_digit: return True
        optimized_digit_ssn = SSN_CODE[optimized_digit]
        #CALCULATE MOVE
        mask = initial_digit_ssn ^ optimized_digit_ssn
        remove_sticks = (initial_digit_ssn & mask).bit_count()
        add_sticks = (optimized_digit_ssn & mask).bit_count()
        new_balance = balance
        moves = 0
        moves += max(min(new_balance, 0) + remove_sticks, 0)
        new_balance += remove_sticks
        moves += max(min(-new_balance, 0) + add_sticks, 0)
        new_balance -= add_sticks
        #VALIDATE MOVE
        if moves > moves_left: continue
        # if pointer != 0:
        #     if new_balance > 0 and new_balance - possible_balance_decrease_digitwise[-pointer-1] > 0: continue
        #     if new_balance < 0 and new_balance + possible_balance_increase_digitwise[-pointer-1] < 0: continue
        #EXECUTE MOVE
        optimized_num[-pointer-1] = optimized_digit
        moves_digitwise[-pointer-1] = moves
        balance_digitwise[-pointer-1] = new_balance - balance
        return True
    return False


while True:
    for pointer in range(pointer -1, -1, -1):
        optimize_digit(pointer, 0xF)
    if sum(balance_digitwise) == 0: break
    for pointer in range(DIGITS):
        if optimize_digit(pointer, optimized_num[-pointer-1] - 1):
            break

print(optimized_num)