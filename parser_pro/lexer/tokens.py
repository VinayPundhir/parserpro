import re


def generate_tokens(input_string: str) -> list:
    """
    functon generates tokens from parser_pro expression.
    conditions are as follows:
        split expression using pipe '|'
        ignore any pipe '|' written in double quotes as it will be treated as constant
    """
    # Define the regular expression pattern
    pattern = r'\s*\|\s*(?=(?:[^"]*"[^"]*")*[^"]*$)'

    # Split the input string using the pattern
    result = re.split(pattern, input_string)

    return result
