from ..decorator import method
from typing import Any
from ..args_validator.is_dict_string import is_dict_string

KEY = ".key"
VALUE = ".value"


@method
def map_list(data: Any, args: str) -> list:
    """
    function implements $map_list functionality of parser

    Args:
        data: str , dict, list
        args: string containing valid python dict.
               e.g. {"new_key":".value"}
              .value is used to access the values of input data

    Returns:
        list containing all dict objects

    """
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
