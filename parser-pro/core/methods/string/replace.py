from ..decorator import method


@method
def replace(data: str, args: str) -> str:
    args = args.split(",")
    return data.replace(args[0].strip('"'), args[1].strip('"'))
