from ..decorator import method
from typing import Any
from core.json_handler.parser import parse


@method
def select(data: Any, args: str):
    args = args.split(",")
    args = [i.strip('"') for i in args]
    res = dict()
    for i in args:
        res[i] = parse(data, i)
    return res
