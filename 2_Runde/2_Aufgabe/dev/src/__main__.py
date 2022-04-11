import random
from itertools import product
from statistics import median as _median
from operations import *

MAX_TRYS = 5

def main(digits):
    numbers = [random.randint(1, 9) for i in range(digits)]
    results = []
    operation_lists = []
    def debug():
        return
        try: print(len(solutions))
        except:
            print(len(list(zip(results, operation_lists))))
    ### GET POSSIBLE SOLUTIONS
    # find all possible solutions
    for operations in product(OPERATIONS, repeat=digits - 1):
        operations = list(operations)
        try: result = evaluateExpression(numbers, operations)
        except EvaluationError: continue
        if result <= 0: continue
        results.append(result)
        operation_lists.append(operations)
    debug()
    # remove duplicated solutions
    for i, result in reversed(list(enumerate(results))):
        if results.count(result) > 1:
            results.pop(i)
            operation_lists.pop(i)
    debug()
    ### REMOVE UNINTRESTING SOLUTIONS
    # remove too boring solutions
    diversitys = [len(set(x)) for x in operation_lists]
    solutions = list(zip(results, operation_lists, diversitys))
    best_diversity = max(diversitys)
    for i, solution in reversed(list(enumerate(solutions))):
        if solution[2] < best_diversity:
            solutions.pop(i)
    del best_diversity
    debug()
    # sort list (after their distance of their result to the average)
    median = _median(results)
    def solutionSorter(solution):
        return abs(median - solution[0])
    solutions.sort(key=solutionSorter)
    del median, solutionSorter
    debug()
    return solutions[0]

digits = 8
numbers = [random.randint(1, 9) for i in range(digits)]

# for numbers in product(range(1, 10), repeat=digits):
#     print(main(digits, list(numbers)))

# print(main(digits, numbers))

for c in range(2, 16):
    for i in range(1):
        print(c, main(c))