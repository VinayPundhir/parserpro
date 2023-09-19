from core.lexer.methods_args import extract_method_and_args, KEY, VALUE


def test_single_arg():
    expr = '$join("|")'
    func_args = extract_method_and_args(expr.lstrip("$"))
    func, args = func_args[0][KEY], func_args[0][VALUE]
    assert func == "join"
    assert args == '"|"'


def test_arg_as_dict():
    expr = '$map_dict({"key-.key":".value"})'
    func_args = extract_method_and_args(expr.lstrip("$"))
    func, args = func_args[0][KEY], func_args[0][VALUE]
    assert func == "map_dict"
    assert args == '{"key-.key":".value"}'
