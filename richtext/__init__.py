from delta import Delta


def create(initial):
    return Delta(initial)


def append(snapshot, delta):  # apply is reserved build-in symbol
    snapshot = Delta(snapshot)
    delta = Delta(delta)
    return snapshot.compose(delta)


def compose(delta1, delta2):
    delta1 = Delta(delta1)
    delta2 = Delta(delta2)
    return delta1.compose(delta2)


def diff(delta1, delta2):
    delta1 = Delta(delta1)
    delta2 = Delta(delta2)
    return delta1.diff(delta2)


def transform(delta1, delta2):
    delta1 = Delta(delta1)
    delta2 = Delta(delta2)
    return delta1.diff(delta2)
