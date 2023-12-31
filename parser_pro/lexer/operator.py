import re


def extract_operators_and_operands(expression: str, operator_list: list) -> tuple:
    """
    function used to extract operator and operands from lexer generated tokens
    """
    for i in operator_list:
        if i in expression:
            operands = [v.strip() for v in expression.split(i)]
            return i, operands
    return None, None
