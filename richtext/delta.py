INFINITY = float('inf')

class Delta(object):

    def __init__(self, ops=[]):
        # Assume we are given a well formed ops
        if isinstance(ops, Delta):
            self.ops = ops.ops
        elif iz.array(ops):
            self.ops = ops
        elif iz.dictionary(ops) and iz.array(ops['ops']):
            self.ops = ops['ops']
        else:
            self.ops = []
        unicode_ops = []
        for op in self.ops:
            if op.get('insert') and iz.string(op['insert']):
                op['insert'] = unicode(op['insert'])
            unicode_ops.append(op)
        self.ops = unicode_ops

    def insert(self, text, attributes=None):
        newOp = {}
        if iz.string(text):
            if not len(text):
                return self
            newOp['insert'] = unicode(text)
        elif iz.number(text):
            newOp['insert'] = text
        if iz.dictionary(attributes) and len(attributes):
            newOp.attributes = attributes
        return self.push(newOp)

    def delete(self, length):
	raise NotImplementedError()

    def retain(self, length, attributes=False):
	raise NotImplementedError()

    def push(self, newOp):
        index = len(self.ops)
        lastOp = self.ops[index - 1] if index else {}
        newOp = op.attributes.clone(newOp)
        if iz.dictionary(lastOp):
            if iz.number(newOp.get('delete')) and iz.number(lastOp.get('delete')):
                self.ops[index - 1] = {'delete': lastOp.get('delete') + newOp.get('delete')}
                return self
        # Since it does not matter if we insert before or after deleting at the same index,
        #  always prefer to insert first
        if iz.number(lastOp.get('delete')) and iz.string(newOp.get('insert')) or iz.number(newOp.get('insert')):
            index -= 1
            lastOp = self.ops[index - 1]
            if not iz.dictionary(lastOp):
                self.ops = [newOp] + self.ops
                return self

        if iz.equal(newOp.get('attributes'), lastOp.get('attributes')):
            if iz.string(newOp.get('insert')) and iz.string(lastOp.get('insert')):
                self.ops[index - 1] = {'insert': lastOp['insert'] + newOp['insert']}
                if iz.dictionary(newOp.get('attributes')):
                    self.ops[index - 1]['attributes'] = newOp['attributes']
                return self
            elif iz.number(newOp.get('retain')) and iz.number(lastOp.get('retain')):
                self.ops[index - 1] = {'retain': lastOp.get('retain') + newOp.get('retain')}
                if iz.dictionary(newOp.get('attributes')):
                    self.ops[index - 1]['attributes'] = newOp.get('attributes')
                return self
        self.ops = self.ops[0:index] + [newOp] + self.ops[index:-1]
        return self

    def length(self):
	raise NotImplementedError()

    def chop(self):
        try:
            lastOp = self.ops[-1]
            if lastOp['retain'] and not lastOp.get('attributes'):
                self.ops.pop()
        except:
            pass
        return self

    def slice(self, start=0, end=INFINITY):
	raise NotImplementedError()

    def compose(self, other):
        other = Delta(other)
        selfIter = op.Iterator(self.ops)
        otherIter = op.Iterator(other.ops)
        self.ops = []
        while selfIter.hasNext() or otherIter.hasNext():
            if otherIter.peekType() == 'insert':
                self.push(otherIter.next())
            elif selfIter.peekType() == 'delete':
                self.push(selfIter.next())
            else:
                length = min(selfIter.peekLength(), otherIter.peekLength())
                selfOp = selfIter.next(length)
                otherOp = otherIter.next(length)
                if iz.number(otherOp.get('retain')):
                    newOp = {}
                    if iz.number(selfOp.get('retain')):
                        newOp['retain'] = length
                    else:
                        newOp['insert'] = selfOp.get('insert')
                    # Preserve null when composing with a retain, otherwise remove it for inserts
                    attributes = op.attributes.compose(
                                                       selfOp.get('attributes'),
                                                       otherOp.get('attributes'),
                                                       iz.number(selfOp.get('retain'))
                                                       )
                    if attributes:
                        newOp['attributes'] = attributes
                    self.push(newOp)
                # Other op should be delete, we could be an insert or retain
                # Insert + delete cancels out
                elif iz.number(otherOp.get('delete')) and iz.number(selfOp.get('retain')):
                    self.push(otherOp)
        return self.chop()

    def diff(self, other):
	raise NotImplementedError()

    def transform(self, other, priority=False):
	raise NotImplementedError()

    def transformPosition(self, index, priority):
	raise NotImplementedError()

