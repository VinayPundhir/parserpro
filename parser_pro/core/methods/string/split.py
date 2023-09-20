from ..decorator import method


@method
def split(data: str, args: str):
    """
    function implements $split functionality of parser
    Args:
        data: str
        args: str as args1 with arg2 (optional , used to set number of time string should ve split )
              where both args should be written in double quotes and separated by ","

    Returns:
        list containing chunks split by arg1
    """
    args = args.split(",")
    args = [i.strip('"') for i in args]
    if len(args) == 1:
        return data.split(args[0])
    elif len(args) == 2:
        return data.split(args[0], int(args[1]))
