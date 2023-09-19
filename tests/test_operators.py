from core.operators import OPERATORS, add
from core.lexer.operator import extract_operators_and_operands
from core.json_handler.parser import parse


def test_add_success():
    data = {
        "hobbies": ["Reading", "Hiking", "Travelling"],
        "age": "30",
        "marks": "34",
        "nums": [1, 2, 3, 4],
    }

    # adding lists
    expr = "hobbies + hobbies"
    operator, operands = extract_operators_and_operands(expr, OPERATORS)
    assert operator == "+"
    operands = [parse(data, i) for i in operands]
    assert add(operands) == [
        "Reading",
        "Hiking",
        "Travelling",
        "Reading",
        "Hiking",
        "Travelling",
    ]

    # adding strings
    expr = "age + marks"
    operator, operands = extract_operators_and_operands(expr, OPERATORS)
    assert operator == "+"
    operands = [parse(data, i) for i in operands]
    assert add(operands) == "3034"

    # adding strings and constant
    expr = '"he is " + age + " but still he got " + marks + " marks"'
    operator, operands = extract_operators_and_operands(expr, OPERATORS)
    assert operator == "+"
    operands = [parse(data, i) for i in operands]
    assert add(operands) == "he is 30 but still he got 34 marks"

    # adding integers
    expr = "nums[1] + nums[3]"
    operator, operands = extract_operators_and_operands(expr, OPERATORS)
    assert operator == "+"
    operands = [parse(data, i) for i in operands]
    assert add(operands) == 6

    # adding integers
    expr = "nums[1] + nums[3]"
    operator, operands = extract_operators_and_operands(expr, OPERATORS)
    assert operator == "+"
    operands = [parse(data, i) for i in operands]
    assert add(operands) == 6


def test_add_fail():
    data = {
        "hobbies": ["Reading", "Hiking", "Travelling"],
        "age": "30",
        "marks": "34",
        "nums": [1, 2, 3, 4],
    }

    # adding lists
    expr = "hobbies + age"
    operator, operands = extract_operators_and_operands(expr, OPERATORS)
    assert operator == "+"
    operands = [parse(data, i) for i in operands]
    assert add(operands) is None

    # adding strings
    expr = "age + nums[1]"
    operator, operands = extract_operators_and_operands(expr, OPERATORS)
    assert operator == "+"
    operands = [parse(data, i) for i in operands]
    assert add(operands) is None

    # adding integers
    expr = "nums + age"
    operator, operands = extract_operators_and_operands(expr, OPERATORS)
    assert operator == "+"
    operands = [parse(data, i) for i in operands]
    assert add(operands) is None
