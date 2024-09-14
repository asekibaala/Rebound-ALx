def class_to_json(obj):
    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res