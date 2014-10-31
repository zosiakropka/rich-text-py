INFINITY = float('inf')

class Delta(object):

    def __init__(self, ops=[]):
	raise NotImplementedError()

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

