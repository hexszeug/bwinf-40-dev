from random import randint

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def times(a, b):
    return a * b

def ratio(a, b):
    res = a / b
    if (not res.is_integer()):
        raise Exception("illegal calculation")
    return int(res)

OPERATIONS = [(plus, minus), (times, ratio)]

term = [3, plus, 5, times, 2]

def resolve(term, depth=0):
    if not isinstance(term, list) or len(term) < 1:
        raise Exception("not a valid term")

    if len(term) == 1:
        return term[0]
    
    op_index = len(OPERATIONS) - (depth + 1)
    if op_index < 0:
        raise Exception("not a valid operation")
    ops = OPERATIONS[op_index]

    i = 0
    while i < int((len(term) - 1) / 2):
        a_index = i*2
        op_index = i*2+1
        b_index = i*2+2
        if term[op_index] in ops:
            term[a_index] = term[op_index](term[a_index], term[b_index])
            term.pop(b_index)
            term.pop(op_index)
        else:
            i += 1
    
    return resolve(term, depth + 1)

print(resolve(term))
