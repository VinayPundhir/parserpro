from ..decorator import method


@method
def join(data: list, args: str) -> str:
    args = args.strip('"')
    return args.join([str(i) for i in data])
