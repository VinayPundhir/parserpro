from functools import wraps


def operator(func):
    """
    This is decorator used to implement operators
    each implemented operator function should take only one arg namely  args:list
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            raise ValueError(f"Error in operator {func.__name__} : {e}")

    return wrapper
