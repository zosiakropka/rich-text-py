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
	raise NotImplementedError()

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

