"""
Examples :

>>> data = [1, 2, 3, 4]
>>> expr = '$map_list({"key":".value"})'
>>> parse(data, expr)
"[{"key":"1"},{"key":"2"},{"key":"3"},{"key":"4"}]"

>>> data = {"name": "parser-pro"}
>>> expr = '$map_dict({"key-.key":".value"})'
>>> parse(data, expr)
"[{"key-name":"parser-pro"}]"

"""
