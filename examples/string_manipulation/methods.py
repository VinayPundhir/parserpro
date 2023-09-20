"""
Examples :

>>> data = {"name": "parser-pro", "address": {"street": "random"}, "nums": [1, 2, 3, 4]}
>>> expr = "address.street | $split("e")"
>>> parse(data, expr)
"['random']"

>>> data = [1, 2, 3, 4]
>>> expr = "$join('|')"
>>> parse(data, expr)
"1|2|3|4"

>>> data = "parser-pro-v.1"
>>> expr = '$replace("v.1", "v.2")'
>>> parse(data, expr)
"parser-pro-v.2"

>>> data = "parser-pro"
>>> expr = '$split("-")'
>>> parse(data, expr)
"['parser', 'pro']"

"""