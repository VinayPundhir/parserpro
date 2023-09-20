from ..decorator import method
from typing import Any
from parser_pro.core.json_handler.parser import parse


@method
def select(data: dict, args: str):
    """
    function implements $select functionality of parser

    Args:
        data: dict
        args: str as "," separated keys , each key written in double quotes

    Returns:
        new dict object combined the selected keys
    """
    args = args.split(",")
    args = [i.strip('"') for i in args]
    res = dict()
    for i in args:
        res[i] = parse(data, i)
    return res
