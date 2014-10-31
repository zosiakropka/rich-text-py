INFINITY = float('inf')

class Delta(object):

    def __init__(self, ops=[]):
        # Assume we are given a well formed ops
        if iz.array(ops):
            self.ops = ops
        elif iz.dictionary(ops) and iz.array(ops['ops']):
            self.ops = ops['ops']
        else:
            self.ops = []
        unicode_ops = []
        for op in self.ops:
            if op.get('insert'):
                op['insert'] = unicode(op['insert'])
            unicode_ops.append(op)
        self.ops = unicode_ops

    def insert(self, text, attributes):
	raise NotImplementedError()

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
	raise NotImplementedError()

    def slice(self, start=0, end=INFINITY):
	raise NotImplementedError()

    def compose(self, other):
	raise NotImplementedError()

    def diff(self, other):
	raise NotImplementedError()

    def transform(self, other, priority=False):
	raise NotImplementedError()

    def transformPosition(self, index, priority):
	raise NotImplementedError()

