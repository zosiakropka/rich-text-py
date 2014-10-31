def equal(a, b):
    return a == b


def array(obj=None):
    return isinstance(obj, list)


def number(obj=None):
    return isinstance(obj, int) or isinstance(obj, float)


def dictionary(obj=None):
    return isinstance(obj, dict)


def string(obj=None):
    return isinstance(obj, str) or isinstance(obj, unicode)

