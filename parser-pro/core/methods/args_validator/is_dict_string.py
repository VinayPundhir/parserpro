import ast


def is_dict_string(arg: str) -> bool:
    """validate if current string arg is a proper dict"""
    try:
        # Attempt to parse the string as a Python literal expression
        parsed_dict = ast.literal_eval(arg)
        # Check if the parsed result is a dictionary
        if isinstance(parsed_dict, dict):
            return True
        else:
            raise ValueError("arg is not a proper dict")
    except (ValueError, SyntaxError) as e:
        # If there's a parsing error, it's not a valid dictionary string
        raise ValueError(f"Error parsing arg {arg} : {e}")
