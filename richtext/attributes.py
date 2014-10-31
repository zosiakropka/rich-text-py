import iz


def clone(attributes, keepNull=False):
    if not iz.dictionary(attributes):
        return {}
    memo = {}
    for key in attributes:
        if key in attributes and (attributes[key] != None or keepNull):
            memo[key] = attributes[key]
    return memo


def compose(a={}, b={}, keepNull=None):
    if not iz.dictionary(a):
        a = {}
    if not iz.dictionary(b):
        b = {}
    attributes = clone(b, keepNull)
    for key in a.keys():
        if key in a and key not in b:
            attributes[key] = a[key]
    return attributes if len(attributes) else None


def diff(a, b):
    if not iz.dictionary(a):
        a = {}
    if not iz.dictionary(b):
        b = {}
    attributes = {}
    for key in a.keys() + b.keys():
        if (key not in a or key not in b) or (a.get(key) != b.get(key)):
            attributes[key] = b.get(key)
    return attributes if len(attributes.keys()) else None


def transform(a, b, priority=False):
    if not iz.dictionary(a):
        return b
    if not iz.dictionary(b):
        return None
    if not priority:
        return b  # b simply overwrites us without priority
    attributes = {}
    for key in b.keys():
        if key not in a:  # None is a valid value
            attributes[key] = b[key]
    return attributes if len(attributes.keys()) else None
