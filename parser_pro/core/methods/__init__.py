from .list.join import join as list_join
from .string.split import split as str_split
from .string.replace import replace as str_replace
from .list.map_list import map_list
from .dict.map_dict import map_dict
from .query.get import get
from .query.select import select
from .filters.condition import eq

METHODS = {
    "join": list_join,
    "split": str_split,
    "replace": str_replace,
    "map_list": map_list,
    "map_dict": map_dict,
    "get": get,
    "select": select,
    "eq": eq,
}


def get_method(name: str):
    if name not in METHODS:
        raise KeyError(f"Unknown method : '{name}'")
    return METHODS[name]
