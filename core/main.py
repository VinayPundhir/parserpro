from core.lexer.tokens import generate_tokens
import core.json_handler.parser as json_parser
from core.lexer.methods_args import extract_method_and_args, KEY, VALUE
from core.lexer.operator import extract_operators_and_operands
from core.operators import OPERATORS
from core.methods import get_method


def parse(data: dict, s: str):
    result = ""

    for chunk in generate_tokens(s):
        operator, operands = extract_operators_and_operands(
            chunk, operator_list=OPERATORS.keys()
        )

        # methods logic
        if chunk.startswith("$"):
            if not result:
                result = data
            for func_and_arg in extract_method_and_args(chunk.lstrip("$")):
                func, args = func_and_arg[KEY], func_and_arg[VALUE]
                result = get_method(func)(result, args)

        # operators logic
        elif operator:
            operands = [parse(data, i) for i in operands]
            result = OPERATORS[operator[0]](operands)

        # json parsing
        else:
            result = json_parser.parse(data, chunk)

    return result
