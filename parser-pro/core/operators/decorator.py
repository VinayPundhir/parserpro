def operator(func):
    """
    Hint : Underlying function should take argument namely  operands:list
    """

    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            raise ValueError(f"Error in operator {func.__name__} : {e}")

    return wrapper
