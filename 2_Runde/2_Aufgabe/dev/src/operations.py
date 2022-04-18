class EvaluationError(Exception):
    pass

def plus(a: int, b: int) -> int:
    return a + b

def minus(a: int, b: int) -> int:
    return a - b

def times(a: int, b: int) -> int:
    return a * b

def divided(a: int, b: int) -> int:
    ratio = a / b
    if ratio.is_integer(): return int(ratio)
    else: raise EvaluationError("division result is no integer number")

OPERATIONS = {
    "+": {
        "name": "plus",
        "key": "+",
        "run": plus
    },
    "-": {
        "name": "minus",
        "key": "-",
        "run": minus
    },
    "*": {
        "name": "times",
        "key": "*",
        "run": times
    },
    "/": {
        "name": "divided",
        "key": "/",
        "run": divided
    }
}

OPERATION_ASSOSIATION_DEPTHS = (
    ("*", "/"),
    ("+", "-")
)

def evaluateExpression(numbers: list, operations: list) -> int:
    numbers_before = numbers.copy()
    operations_before = operations.copy()
    for associative_operations in OPERATION_ASSOSIATION_DEPTHS:
        numbers_after = [numbers_before[0]]
        operations_after = operations_before.copy()
        for i, operation_key in enumerate(operations_before):
            if operation_key not in associative_operations:
                numbers_after.append(numbers_before[i+1])
                continue
            numbers_after[-1] = OPERATIONS[operation_key]["run"](numbers_after[-1], numbers_before[i+1])
            operations_after.remove(operation_key)
        numbers_before = numbers_after
        operations_before = operations_after
    return numbers_before[0]