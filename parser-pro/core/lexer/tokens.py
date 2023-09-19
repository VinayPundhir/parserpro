import re


def generate_tokens(input_string: str) -> list:
    """info : splits the expression into statements
    expression is separated by '|' without quotes and ignores any '|' in double quotes
    """
    # Define the regular expression pattern
    pattern = r'\s*\|\s*(?=(?:[^"]*"[^"]*")*[^"]*$)'

    # Split the input string using the pattern
    result = re.split(pattern, input_string)

    return result
