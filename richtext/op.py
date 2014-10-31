import attributes
import iz


def clone(op):
    newOp = attributes.clone(op)
    if iz.dictionary(newOp.get('attributes')):
        newOp['attributes'] = attributes.clone(newOp.attributes, True)
    return newOp


def iterator(op):
    from iterator import Iterator
    return Iterator(op)


def length(op):
    if iz.number(op.get('delete')):
        return op['delete']
    elif iz.number(op.get('retain')):
        return op['retain']
    else:
        return len(op['insert']) if iz.string(op.get('insert')) else 1
