import re


def extract_operators_and_operands(expression: str, operator_list: list) -> tuple:
    for i in operator_list:
        if i in expression:
            operands = [v.strip() for v in expression.split(i)]
            return i, operands
    return None, None


# def extract_operators_and_operands(expression:str, operator_list:list)->tuple:
#     for op in operator_list:
#         pattern = r"(?![\"\']).[OPERATORS](?![\"\'])"
#         pattern = pattern.replace("OPERATORS", op)
#         result = re.split(pattern, expression)
#         result = [i.strip() for i in result]
