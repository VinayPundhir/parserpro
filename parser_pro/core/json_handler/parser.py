def parse(json_data: dict, path: str):
    """
    function used to parse complex python objects using "." operator for nested dict and [i] for lists where i is index of list
    """
    if path.startswith(('"', "'")) and path.endswith(('"', "'")):
        return path.strip('"')

    def get_value(obj, part):
        if isinstance(obj, dict):
            return obj.get(part)
        elif isinstance(obj, list):
            if part == "[*]":
                return obj
            try:
                index = int(part.strip("[]"))
                return obj[index]
            except (ValueError, IndexError):
                return None
        else:
            return None

    parts = path.split(".")
    result = json_data

    for part in parts:
        if result is None:
            break
        if "[" in part:
            subparts = part.split("[")
            for subpart in subparts:
                result = get_value(result, subpart.strip("]"))
        else:
            result = get_value(result, part)

    return result
