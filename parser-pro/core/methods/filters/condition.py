from ..decorator import method


@method
def eq(data: list, args: str):
    args = args.split(",")
    args = [i.strip('"') for i in args]

    if len(args) != 2:
        raise ValueError("args length should be 2")

    res = []
    for obj in data:
        if type(obj) != dict:
            raise TypeError("Data should be list containing dict")

        if args[0] in obj and obj[args[0]] == args[1]:
            res.append(obj)

    return res
