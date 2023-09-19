from ..decorator import operator


@operator
def add(operands: list):
    if None in operands:
        raise ValueError(f"can not perform operation + between \n {operands}")

    for dtype_value in [list(), 0, "", tuple()]:
        if all([type(i) == type(dtype_value) for i in operands]):
            res = dtype_value
            for v in operands:
                res += v
            return res

    for dtype_value in [{}]:
        if all([type(i) == type(dtype_value) for i in operands]):
            res = dict()
            for obj in operands:
                for k, v in obj.items():
                    res[k] = v
            return res
