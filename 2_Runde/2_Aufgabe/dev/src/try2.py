from itertools import combinations_with_replacement
import numbers

def plus(a: int, b: int) -> int:
    return a + b

def minus(a: int, b: int) -> int:
    return a - b

def times(a: int, b: int) -> int:
    return a * b

def divided(a: int, b: int) -> int:
    ratio = a / b
    if ratio.is_integer(): return int(ratio)
    else: return None

OPERATIONS = [[times, divided], [plus, minus]]

def solve(numbers: list, operations: list):
    operations = list(operations)
    for op_list in OPERATIONS:
        result = [numbers[0]]
        operations_left = operations[:]
        for i, op in enumerate(operations):
            if op in op_list:
                result[-1] = op(result[-1], numbers[i+1])
                if result[-1] == None: return None
                operations_left.remove(op)
            else:
                result.append(numbers[i+1])
        numbers = result
        operations = operations_left
    return numbers[0]

def operation_combis(digits: int):
    return combinations_with_replacement([y for x in OPERATIONS for y in x], digits - 1)

def find_positive_integer_solutions(numbers: list):
    solutions = []
    operation_list = []
    for operations in operation_combis(len(numbers)):
        result = solve(numbers, operations)
        if result == None or result <= 0: continue
        solutions.append(result)
        operation_list.append(operations)
    return solutions, operation_list

def find_unique_solutions(numbers: list):
    solutions, operation_list = find_positive_integer_solutions(numbers)
    duplicates = []
    print(solutions)
    for i, solution in enumerate(solutions):
        if solutions.count(solution) > 1:
            duplicates.append(i)
            print(i, solution)
    duplicates.reverse()
    for i in duplicates:
        solutions.pop(i)
        operation_list.pop(i)
    return solutions, operation_list

numbers = [5, 8, 3, 1, 6]

print(find_unique_solutions(numbers))

# for d in range(2, 16):
#     print(f"{d}-------------------")
#     for n in combinations_with_replacement(range(1, 10), d):
#         s = find_unique_solutions(n)
#         if len(s) < 2: print(n)
