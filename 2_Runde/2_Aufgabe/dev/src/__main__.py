import random
import argparse
from itertools import product as _product, chain as _chain
from statistics import median as _median

from operations import *

#parse arguments
argparser = argparse.ArgumentParser()
argparser.add_argument("operation_count", type=int, help="count of the operations to guess in the output rizzle")
args = argparser.parse_args()
digits = args.operation_count + 1
if digits < 2:
    exit("The operation count must not be less than 1")

#generate numbers
numbers = [random.randint(1, 9) for i in range(digits)]

#calculate results for substituting every possible operation combination between "numbers"
results = []
operation_lists = []
for operations in _product(OPERATIONS, repeat=digits - 1):
    operations = list(operations)
    try: result = evaluateExpression(numbers, operations)
    except EvaluationError: continue
    if result <= 0: continue
    results.append(result)
    operation_lists.append(operations)

#remove duplicated solutions
for i, result in reversed(list(enumerate(results))):
    if results.count(result) > 1:
        results.pop(i)
        operation_lists.pop(i)

#remove too boring solutions
diversitys = [len(set(x)) for x in operation_lists]
solutions = list(zip(results, operation_lists, diversitys))
best_diversity = max(diversitys)
for i, solution in reversed(list(enumerate(solutions))):
    if solution[2] < best_diversity:
        solutions.pop(i)
del best_diversity

#sort list (after their distance of their result to the median of all results)
median = _median(results)
def solutionSorter(solution):
    return abs(median - solution[0])
solutions.sort(key=solutionSorter)
del median, solutionSorter

#output solution #TODO make better

output_solution = random.choices(solutions, weights=reversed(list(range(len(solutions)))))[0]

solution_str = f"{''.join(list(_chain(*list(zip([str(x) for x in numbers], output_solution[1])))))}{numbers[-1]}"
exec(f"calculated_result = int({solution_str})")

print(f"{'?'.join([str(x) for x in numbers])}={output_solution[0]}")
print(f"{solution_str}={calculated_result}")