import random
from itertools import combinations_with_replacement
from operations import *

MAX_TRYS = 5

def main(digits):
    trys = []
    for tri in range(MAX_TRYS):
        numbers = [random.randint(1, 9) for i in range(digits)]
        results = []
        operation_lists = []
        def debug(): #TODO remove debug function
            try: print(solutions)
            except:
                print(results)
                print(operation_lists)
        ### GET POSSIBLE SOLUTIONS
        # find all possible solutions
        for operations in combinations_with_replacement(\
            [x for x in OPERATIONS],\
            len(numbers) - 1\
        ):
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
        max_diversity = max(diversitys)
        for i in range(len(results) -1, -1, -1):
            if diversitys[i] < max_diversity:
                results.pop(i)
                operation_lists.pop(i)
        solutions = list(zip(results, operation_lists, diversitys))
        del max_diversity
        debug()
        # sort list (after their distance of their result to the average)
        average = sum(results) / len(results)
        def solutionSorter(solution):
            return abs(average - solution[0])
        solutions.sort(key=solutionSorter)
        del average, solutionSorter
        debug()

main(5)
# for c in range(2, 16):
#     test = [len(set(main(c, list(numbers))[0][1])) for numbers in combinations_with_replacement(range(1, 10), c)]
#     print(c, sum(test) / len(test))