from typing import Any
from ..decorator import method


@method
def get(data: Any, args: str):
    """
    functon implements $get functionality of parser
    Args:
        data: str , list or any data type where index can be applied
        args: index in double quotes e.g "0"
              range of index can be given as "1","4"

    Returns:
        subset of data in given index or range
    """
    args = args.split(",")
    args = [i.strip('"') for i in args]
    for arg in args:
        if not arg.isdigit():
            ValueError(f"args to function 'get' should be string containing index")

    if len(args) == 1:
        return data[int(args[0])]
    elif len(args) == 2:
        return data[int(args[0]) : int(args[1])]
