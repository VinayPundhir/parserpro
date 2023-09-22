from ..decorator import method


@method
def replace(data: str, args: str) -> str:
    """
    function implements $replace functionality of parser
    Args:
        data: str
        args: str as args1 with arg2 where both args should be written in double quotes and seperated by ","

    Returns:
        replaced string with arg2 where in place of arg1
    """
    args = args.split(",")
    return data.replace(args[0].strip('"'), args[1].strip('"'))
