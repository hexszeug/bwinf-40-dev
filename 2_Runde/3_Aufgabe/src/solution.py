from ssncode import SSN_CODE

def get_best_number(initial_num, max_moves):
    #setup initial constants
    INITIAL_NUM = initial_num
    MAX_MOVES = max_moves
    DIGITS = len(INITIAL_NUM)

    #precalculate balance limits for each digit
    ssncode_stick_counts = [x.bit_count() for x in SSN_CODE]
    max_stick_count = max(ssncode_stick_counts)
    min_stick_count = min(ssncode_stick_counts)
    balance_max_limits = [0]
    balance_min_limits = [0]
    rev_num = INITIAL_NUM[:]
    rev_num.reverse()
    for digit in rev_num:
        balance_max_limits.insert(0, max_stick_count - SSN_CODE[digit].bit_count() + balance_max_limits[0])
        balance_min_limits.insert(0, min_stick_count - SSN_CODE[digit].bit_count() + balance_min_limits[0])
    balance_max_limits.pop(0)
    balance_min_limits.pop(0)
    del ssncode_stick_counts, max_stick_count, min_stick_count, rev_num
    
    #setup initial variables
    optimized_num = [0x10] * DIGITS #number which approaches solution
    moves_digitwise = [0] * DIGITS #moves each digit caused (according to current optimized_num state)
    balance_digitwise = [0] * DIGITS #balance change each digit caused (according to current optimized_num state)
    pointer = DIGITS #pointer to currently processed digit

    #calculate best number
    def optimize_digit(pointer, preferred_digit):
        moves_left = MAX_MOVES - sum(moves_digitwise[:-pointer-1])
        balance = sum(balance_digitwise[:-pointer-1])
        initial_digit = INITIAL_NUM[-pointer-1]
        initial_digit_ssn = SSN_CODE[initial_digit]
        for digit_attempt in range(preferred_digit, -1, -1): #try each digit (preferred to 0) decreasing attempted digit if it wasnt possible
            #calculate consequences of changing digit to attempt
            digit_attempt_ssn = SSN_CODE[digit_attempt]
            mask = initial_digit_ssn ^ digit_attempt_ssn
            remove_sticks = (initial_digit_ssn & mask).bit_count() #count sticks to remove
            add_sticks = (digit_attempt_ssn & mask).bit_count() #count sticks to add
            new_balance = balance
            moves = 0
            moves += max(min(new_balance, 0) + remove_sticks, 0)
            new_balance += remove_sticks
            moves += max(min(-new_balance, 0) + add_sticks, 0)
            new_balance -= add_sticks
            #check if digit change is possible
            if moves > moves_left: continue #costs to much moves -> lower attempt
            if new_balance > balance_max_limits[-pointer-1] or new_balance < balance_min_limits[-pointer-1]: continue #pushes balance to high -> lower attempt
            #change digit
            optimized_num[-pointer-1] = digit_attempt
            moves_digitwise[-pointer-1] = moves
            balance_digitwise[-pointer-1] = new_balance - balance
            return True
        return False #cant change digit (somthing a digit before went wrong)
    while pointer > 0:
        pointer -= 1 #decreas pointer
        if not optimize_digit(pointer, optimized_num[-pointer-1] - 1):
            pointer += 2 #increase pointer cause something went wrong (to redo last digit)
    
    return optimized_num, sum(moves_digitwise)