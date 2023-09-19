from typing import Any
from ..decorator import method


@method
def get(data: Any, args: str):
    args = args.split(",")
    args = [i.strip('"') for i in args]
    for arg in args:
        if not arg.isdigit():
            ValueError(f"args to function 'get' should be string containing index")

    if len(args) == 1:
        return data[int(args[0])]
    elif len(args) == 2:
        return data[int(args[0]) : int(args[1])]
