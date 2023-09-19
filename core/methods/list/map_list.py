from ..decorator import method
from typing import Any
from ..args_validator.is_dict_string import is_dict_string

KEY = ".key"
VALUE = ".value"


@method
def map_list(data: Any, args: str):
    """used to deal with only values"""
    is_dict_string(args)

    if type(data) == dict:
        data = data.values()
    elif type(data) == str:
        data = [i for i in data]
    elif type(data) == list:
        data = data
    else:
        raise ValueError("supported type [dict,str,list]")
    return [args.replace(VALUE, str(i)) for i in data]
