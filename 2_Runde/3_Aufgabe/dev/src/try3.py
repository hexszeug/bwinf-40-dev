import sevensegmentnumbers1 as ssn_converter

# def trans(x, y, balance):
#     mask = x ^ y
#     rem = (x & mask).bit_count()
#     add = (y & mask).bit_count()

#     moves = 0
#     moves += min(balance, 0) + rem
#     balance += rem
#     moves += max(balance, 0) + add
#     balance -= add

def optimize_digit(digit, preferred_digit, moves_left, balance):
    digit_ssn = ssn_converter.convert(digit)
    for optimized_digit in range(preferred_digit, -1, -1):
        if optimized_digit == digit: raise Exception("Already optimized")
        optimized_digit_ssn = ssn_converter.convert(optimized_digit)
        mask = digit_ssn ^ optimized_digit_ssn
        rem = (digit_ssn & mask).bit_count()
        add = (optimized_digit_ssn & mask).bit_count()
        new_balance = balance
        moves = 0
        moves += max(min(new_balance, 0) + rem, 0)
        new_balance += rem
        moves += max(min(-new_balance, 0) + add, 0)
        new_balance -= add
        if moves <= moves_left:
            return optimized_digit, moves, new_balance - balance
    raise Exception("Already optimized")


BASE = 16

INITIAL_NUM = [int(x, BASE) for x in list("1A02B6B50D7489D7708A678593036FA265F2925B21C28B4724DD822038E3B4804192322F230AB7AF7BDA0A61BA7D4AD8F888")]
MAX_MOVES = 87
DIGITS = len(INITIAL_NUM)

optimized_num = INITIAL_NUM[:]
moves_digitwise = [0] * DIGITS
balance_digitwise = [0] * DIGITS
pointer = DIGITS

# print(INITIAL_NUM)

while True:
    for pointer in range(pointer -1, -1, -1):
        #TODO finish when balance and moves = 0
        initial_digit = INITIAL_NUM[-pointer-1]
        moves_left = MAX_MOVES - sum(moves_digitwise[:-pointer-1])
        balance = sum(balance_digitwise[:-pointer-1])
        try: optimized_digit, moves, balance = optimize_digit(initial_digit, 0xF, moves_left, balance)
        except Exception: continue
        optimized_num[-pointer-1] = optimized_digit
        moves_digitwise[-pointer-1] = moves
        balance_digitwise[-pointer-1] = balance
    # print("end of rightwards (type A)", sum(moves_digitwise), sum(balance_digitwise), optimized_num[-40:])
    if sum(balance_digitwise) == 0:
        break
    for pointer in range(len(INITIAL_NUM)):
        initial_digit = INITIAL_NUM[-pointer-1]
        preferred_digit = optimized_num[-pointer-1] - 1
        moves_left = MAX_MOVES - sum(moves_digitwise[:-pointer-1])
        balance = sum(balance_digitwise[:-pointer-1])
        try: optimized_digit, moves, balance = optimize_digit(initial_digit, preferred_digit, moves_left, balance)
        except Exception: continue
        optimized_num[-pointer-1] = optimized_digit
        moves_digitwise[-pointer-1] = moves
        balance_digitwise[-pointer-1] = balance
        break
    # print("end of leftwards  (type B)", sum(moves_digitwise), sum(balance_digitwise), optimized_num[-40:])

print(optimized_num)
# print(moves_digitwise)
# print(balance_digitwise)

