"""
Examples :

>>> data = {"name": "parser-pro", "address": {"street": "random"}, "nums": [1, 2, 3, 4]}
>>> expr = "address.street"
>>> parse(data, expr)
"random"

>>> data = {"name": "parser-pro", "address": {"street": "random"}, "nums": [1, 2, 3, 4]}
>>> expr = "nums[1]"
>>> parse(data, expr)
"2"

>>> data = {"name": "parser-pro", "address": {"street": "random"}, "nums": [1, 2, 3, 4]}
>>> expr = "nums"
>>> parse(data, expr)
"[1, 2, 3, 4]"


"""