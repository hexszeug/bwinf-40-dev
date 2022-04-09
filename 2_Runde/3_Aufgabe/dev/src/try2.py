import sevensegmentnumbers as ssn

def transformation_stats(x_ssn, y_ssn, balance):
    """Takes two seven segment numbers and a balance and outputs the change of the balance and the change of m"""
    mask = x_ssn ^ y_ssn
    remove = (x_ssn & mask).bit_count()
    add = (y_ssn & mask).bit_count()
    balance_change = remove - add
    m_change_remove = abs(balance + remove)




initial_hex = "A5"

m_initial = 2



initial_bin = int(initial_hex, 16)

n = len(initial_hex)

x_bin = initial_bin
m = m_initial
balance = 0
pointer = n - 1

while pointer != 0 or balance != 0:
    for pointer in range(pointer, -1, -1): #iterate over digits from left to right, starting at pointer
        x_digit_bin = initial_bin >> (4*pointer) & 0xF #extract digit from initial number
        print(hex(x_digit_bin), hex(x_bin), balance)
        x_bin = ~(0xF << (4*pointer)) & x_bin #clear digit in x
        x_digit_ssn = ssn.bin_digit_to_ssn(x_digit_bin) #generate ssn of x
        for y_digit_bin in range(0xF, -1, -1):  #iterate over possible y, starting with highest
            y_digit_ssn = ssn.bin_digit_to_ssn(y_digit_bin) #generate ssn of y
            changes_mask = x_digit_ssn ^ y_digit_ssn #generate mask to mask out changes from x to y
            remove = (x_digit_ssn & changes_mask).bit_count() #count sticks to remove from x / add to balance
            add = (y_digit_ssn & changes_mask).bit_count() #count sticks to add to x / remove from balance
            balance_change = remove - add #calculate balance change
            m_change = (balance < 0)*add + (balance > 0)*remove + (balance == 0)*max(remove, add) #calculate change of m
            print(bin(x_digit_ssn), hex(x_digit_bin))
            print(bin(changes_mask), remove, add, balance_change, m_change)
            print(bin(y_digit_ssn), hex(y_digit_bin))
            if m_change > m: #y is too high (transformation not possible)
                continue #next y
            m -= m_change #confirm m change
            balance += balance_change #confirm balance change
            x_bin = y_digit_bin << (4*pointer) | x_bin #confirm x change
            break #next x
        print(hex(x_digit_bin), hex(x_bin))
        print("")
    if balance == 0:
        print("hi", hex(x_bin), balance, m)
        break
    for pointer in range(n):
        x_digit_bin = initial_bin >> (4*pointer) & 0xF #extract digit from initial number
        x_digit_bin_ch = x_bin >> (4*pointer) & 0xF #extract digit from x
        x_bin = ~(0xF << (4*pointer)) & x_bin #clear digit in x
        changed = False
        for y_digit_bin in range(x_digit_bin_ch -1, -1, -1):
            y_digit_ssn = ssn.bin_digit_to_ssn(y_digit_bin) #generate ssn of y
            changes_mask = x_digit_ssn ^ y_digit_ssn #generate mask to mask out changes from x to y
            remove = (x_digit_ssn & changes_mask).bit_count() #count sticks to remove from x / add to balance
            add = (y_digit_ssn & changes_mask).bit_count() #count sticks to add to x / remove from balance
            balance_change = remove - add #calculate balance change
            m_change = (balance < 0)*add + (balance > 0)*remove + (balance == 0)*max(remove, add) #calculate change of m
            print(bin(x_digit_ssn), hex(x_digit_bin))
            print(bin(changes_mask), remove, add, balance_change, m_change)
            print(bin(y_digit_ssn), hex(y_digit_bin))
            if m_change > m: #y is too high (transformation not possible)
                continue #next y
            m -= m_change #confirm m change
            balance += balance_change #confirm balance change
            x_bin = y_digit_bin << (4*pointer) | x_bin #confirm x change
            changed = True
            break #next x
        if changed:
            pointer -= 1
            break
