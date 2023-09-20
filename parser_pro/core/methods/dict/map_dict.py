from ..decorator import method
from ..args_validator.is_dict_string import is_dict_string

KEY = ".key"
VALUE = ".value"


@method
def map_dict(data: dict, args: str):
    """
    function implements $map_dict functionality of parser
    Args:
        data: dict
        args:string containing dict e.g {"name":".key","place":".value"}
              .key and .value are used to access the key and value of data
    Returns:
        list containing dict objects e.g [{},{}]
    """
    is_dict_string(args)

    res = []
    for k, v in data.items():
        res.append(args.replace(KEY, str(k)).replace(VALUE, str(v)))
    return res
