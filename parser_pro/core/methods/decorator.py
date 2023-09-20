from typing import Any


def method(func):
    """
    This is a decorator used to implement methods used in parser

        Hint:
            checks compatibility of input data with method args
            each implemented method will take 2 args namely ( data , args ).
            Type of each arg is optional but type hint should be given
    """

    def wrapper(*args, **kwargs):
        try:
            annotations = func.__annotations__
            if (
                type(args[0]) != annotations["data"]
                or type(args[1]) != annotations["args"]
            ):
                if annotations["data"] != Any:
                    raise ValueError(
                        f"{func} takes arguments data:{annotations['data']},args:{annotations['args']} "
                        f"but provided data:{args[0]},args:{args[1]}"
                    )
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            raise ValueError(f"Error in method '{func.__name__}' : \n {e}")

    return wrapper
