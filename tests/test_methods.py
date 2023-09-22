from parser_pro import parse


def test_join():
    data = [1, 2, 3, 4]
    expr = '$join("|")'
    assert parse(data, expr) == "1|2|3|4"


def test_map_list():
    data = [1, 2, 3, 4]
    expr = '$map_list({"key":".value"})'
    assert parse(data, expr) == [
        '{"key":"1"}',
        '{"key":"2"}',
        '{"key":"3"}',
        '{"key":"4"}',
    ]


def test_map_dict():
    data = {"name": "parser-pro"}
    expr = '$map_dict({"key-.key":".value"})'
    assert parse(data, expr) == ['{"key-name":"parser-pro"}']


def test_replace():
    data = "parser-pro-v.1"
    expr = '$replace("v.1","v.2")'
    assert parse(data, expr) == "parser-pro-v.2"


def test_split():
    data = "parser-pro"
    expr = '$split("-")'
    assert parse(data, expr) == ["parser", "pro"]


def test_get_single_value_from_list():
    data = ["parser", "pro"]
    expr = '$get("0")'
    assert parse(data, expr) == "parser"


def test_get_multiple_values_from_list():
    data = ["parser", "pro", "v", "1.0"]
    expr = '$get("1","3")'
    assert parse(data, expr) == ["pro", "v"]


def test_get_value_from_string():
    data = "parser-pro"
    expr = '$get("2","7")'
    assert parse(data, expr) == "rser-"


def test_select():
    data = {"name": "parser", "postfix": "v-0.1"}
    expr = '$select("name","postfix")'
    assert parse(data, expr) == {"name": "parser", "postfix": "v-0.1"}
