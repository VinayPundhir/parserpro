from ..decorator import method


@method
def join(data: list, args: str) -> str:
    """
    function implements $join functionality of parser

    Args:
        data: list of items , where items can be list,tuple,str,int,dict
        args: str containing substring to join all the items

    Returns: single string containing all the joined items

    """
    args = args.strip('"')
    return args.join([str(i) for i in data])
