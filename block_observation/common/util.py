def optional_dict(obj: dict, property: str):
    return obj[property] if property in obj else None
