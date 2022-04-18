import argparse
from random import randint as _randint, choices as _choices
from itertools import product as _product
from statistics import median as _median

#int overloading hack for not allowing divison fraction results
class DivisionResultNotInteger(Exception): ...

class NoFractionInt(int):
    def __add__(self, __x: int) -> int:
        return NoFractionInt(super().__add__(__x))
    def __radd__(self, __x: int) -> int:
        return NoFractionInt(super().__radd__(__x))

    def __sub__(self, __x: int) -> int:
        return NoFractionInt(super().__sub__(__x))
    def __rsub__(self, __x: int) -> int:
        return NoFractionInt(super().__rsub__(__x))

    def __mul__(self, __x: int) -> int:
        return NoFractionInt(super().__mul__(__x))
    def __rmul__(self, __x: int) -> int:
        return NoFractionInt(super().__rmul__(__x))

    def __truediv__(self, __x: int) -> int:
        __r = super().__truediv__(__x)
        if __r.is_integer(): return NoFractionInt(__r)
        raise DivisionResultNotInteger()
    def __rtruediv__(self, __x: int) -> int:
        __r = super().__rtruediv__(__x)
        if __r.is_integer(): return NoFractionInt(__r)
        raise DivisionResultNotInteger()

#parse arguments
argparser = argparse.ArgumentParser()
argparser.add_argument("operation_count", type=int, help="count of the operations to guess in the output rizzle")
args = argparser.parse_args()
digits = args.operation_count + 1
if digits < 2:
    exit("The operation count must not be less than 1")

#generate numbers
numbers = [_randint(1, 9) for i in range(digits)]

#calculate results for substituting every possible operation combination between "numbers"
results = []
operation_lists = []
for operations in _product(["+", "-", "*", "/"], repeat=digits - 1):
    operations = list(operations)
    expression = "".join([f"NoFractionInt({x}){y}" for x, y in zip(numbers, operations)]) + f"NoFractionInt({numbers[-1]})"
    try: result = eval(expression)
    except DivisionResultNotInteger: continue
    if result <= 0: continue
    results.append(int(result))
    operation_lists.append(operations)

#remove duplicated solutions
results_with_duplicates = results.copy()
for i, result in reversed(list(enumerate(results))):
    if results_with_duplicates.count(result) > 1:
        results.pop(i)
        operation_lists.pop(i)
del results_with_duplicates

#remove too boring solutions
diversitys = [len(set(x)) for x in operation_lists]
rizzles = list(zip(results, operation_lists, diversitys))
best_diversity = max(diversitys)
for i, solution in reversed(list(enumerate(rizzles))):
    if solution[2] < best_diversity:
        rizzles.pop(i)
del best_diversity

#sort list (after their distance of their result to the median of all results)
median = _median(results)
def solutionSorter(rizzle):
    return abs(median - rizzle[0])
rizzles.sort(key=solutionSorter)
del median, solutionSorter

#select solution
weights = list(reversed(list(range(1, 1+len(rizzles)))))
output_rizzle = _choices(rizzles, weights=weights)[0]

#output rizzle
print(end="\n\n")
print("◦".join([str(x) for x in numbers]) + "=" + str(output_rizzle[0]), end="\n\n")
print("".join([str(x) + y for x, y in zip(numbers, output_rizzle[1])]) + str(numbers[-1]) + "=" + str(output_rizzle[0]), end="\n\n")
print(end="\n\n")
