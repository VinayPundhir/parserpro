from ..decorator import method


@method
def split(data: str, args: str):
    args = args.split(",")
    args = [i.strip('"') for i in args]
    if len(args) == 1:
        return data.split(args[0])
    elif len(args) == 2:
        return data.split(args[0], int(args[1]))
