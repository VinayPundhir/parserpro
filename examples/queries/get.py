"""
Examples :

>>> data = "parser-pro"
>>> expr = '$get("2","7")'
>>> parse(data, expr)
"rser-"

>>> data = ["parser", "pro"]
>>> expr = "$get('0')"
>>> parse(data, expr)
"parser"

>>> data = ["parser", "pro", "v", "1.0"]
>>> expr = "$get('1', '3')"
>>> parse(data, expr)
"['pro', 'v']"

"""