from parser_pro.json_handler.parser import parse


def test_parse():
    data = {"name": "parser-pro", "address": {"street": "random"}, "nums": [1, 2, 3, 4]}
    expr = "name"
    result = parse(data, expr)
    assert result == "parser-pro"
    expr = "address.street"
    assert parse(data, expr) == "random"
    expr = "nums"
    assert parse(data, expr) == [1, 2, 3, 4]
    expr = "nums[1]"
    assert parse(data, expr) == 2
