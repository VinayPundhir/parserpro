from core.main import parse


def test_get_value_from_string():
    data = {
        "data": [
            {"id": "1", "name": "parser"},
            {"id": "2", "name": "pro"},
            {"id": "3", "name": "v1.0"},
        ]
    }
    expr = 'data | $eq("id","2")'
    assert parse(data, expr) == [{"id": "2", "name": "pro"}]
