"""
Examples :

>>> data = {"name": "parser", "postfix": "v-0.1"}
>>> expr = '$select("name","postfix")'
>>> parse(data, expr)
"{'name': 'parser', 'postfix': 'v-0.1'}"

"""