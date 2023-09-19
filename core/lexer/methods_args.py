KEY = "function"
VALUE = "args"
ARGS_SEPERATOR = ","


def extract_method_and_args(input_string: str) -> list:
    results = []

    func, args = input_string.strip(")").split("(")

    if not func or not args:
        raise ValueError(f"unable to extract function or args : {input_string}")

    results.append({KEY: func, VALUE: args})

    return results
