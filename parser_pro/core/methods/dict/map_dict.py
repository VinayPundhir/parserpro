from ..decorator import method
from ..args_validator.is_dict_string import is_dict_string

KEY = ".key"
VALUE = ".value"


@method
def map_dict(data: dict, args: str):
    """used to deal with both key and values"""
    is_dict_string(args)

    res = []
    for k, v in data.items():
        res.append(args.replace(KEY, str(k)).replace(VALUE, str(v)))
    return res
