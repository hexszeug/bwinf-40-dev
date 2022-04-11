import random
from itertools import product
from operations import *

MAX_TRYS = 5

def main(digits):
    trys = []
    best_try_diversity = 0
    for tri in range(MAX_TRYS):
        numbers = [random.randint(1, 9) for i in range(digits)]
        results = []
        operation_lists = []
        ### GET POSSIBLE SOLUTIONS
        # find all possible solutions
        for operations in product(OPERATIONS, repeat=digits - 1):
            operations = list(operations)
            try: result = evaluateExpression(numbers, operations)
            except EvaluationError: continue
            if result <= 0: continue
            results.append(result)
            operation_lists.append(operations)
        # remove duplicated solutions
        for i, result in reversed(list(enumerate(results))):
            if results.count(result) > 1:
                results.pop(i)
                operation_lists.pop(i)
        ### REMOVE UNINTRESTING SOLUTIONS
        # remove too boring solutions
        diversitys = [len(set(x)) for x in operation_lists]
        solutions = list(zip(results, operation_lists, diversitys))
        best_diversity = max(diversitys)
        for i, solution in reversed(list(enumerate(solutions))):
            if solution[2] < best_diversity:
                solutions.pop(i)
        del best_diversity
        # sort list (after their distance of their result to the average)
        average = sum(results) / len(results)
        def solutionSorter(solution):
            return abs(average - solution[0])
        solutions.sort(key=solutionSorter)
        del average, solutionSorter
        trys.append(solutions)
        if solutions[0][2] > best_try_diversity:
            best_try_diversity = solutions[0][2]
    return [x for x in trys if x[0][2] == best_try_diversity][0][0]

print(main(5))

# for c in range(2, 16):
#     for i in range(1):
#         print(c, main(c))