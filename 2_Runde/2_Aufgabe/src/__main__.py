from itertools import combinations_with_replacement
from operations import *

def main():
    numbers = [5, 8, 3, 1, 6]
    solutions = []
    operation_lists = []
    # find all possible solutions
    for operations in combinations_with_replacement(\
        [x for x in OPERATIONS],\
        len(numbers) - 1\
    ):
        operations = list(operations)
        try: result = evaluateExpression(numbers, operations)
        except EvaluationError: continue
        if result <= 0: continue
        solutions.append(result)
        operation_lists.append(operations)
    # find duplicates
    duplicates = []
    for i, solution in enumerate(solutions):
        if solutions.count(solution) > 1:
            duplicates.append(i)
    # remove duplicates
    duplicates.reverse()
    for i in duplicates:
        solutions.pop(i)
        operation_lists.pop(i)
    del duplicates

main()