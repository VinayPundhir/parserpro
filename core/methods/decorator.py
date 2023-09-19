from typing import Any


def method(func):
    """
    Hint : Underlying function should take two arguments namely : data, args
           Type of each argument is subjected to function usage
           Type hint is mandatory for each argument e.g. data:str,args:list
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
