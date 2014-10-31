Infinity = float('inf')

import op
import iz


class Iterator(object):

    def __init__(self, ops):
        self.ops = ops
        self.index = 0
        self.offset = 0

    def hasNext(self):
        return self.peekLength() < Infinity

    def next(self, length=Infinity):

        nextOp = None
        try:
            nextOp = self.ops[self.index]
        except:
            pass
        if nextOp:
            offset = self.offset
            opLength = op.length(nextOp)
            if length >= opLength - offset:
                length = opLength - offset
                self.index += 1
                self.offset = 0
            else:
                self.offset += length
            if iz.number(nextOp.get('delete')):
                return {'delete': length}
            else:
                retOp = {}
                if nextOp.get('attributes'):
                    retOp['attributes'] = nextOp['attributes']
                if iz.number(nextOp.get('retain')):
                    retOp['retain'] = length
                elif iz.string(nextOp['insert']):
                    retOp['insert'] = nextOp['insert'][offset:(offset + length)]
                else:
                    # offset should === 0, length should === 1
                    retOp['insert'] = nextOp['insert']
                return retOp
        return {'retain': Infinity}

    def peekLength(self):
        try:
            self.ops[self.index]
            # Should never return 0 if our index is being managed correctly
            return op.length(self.ops[self.index]) - self.offset
        except IndexError, e:
            pass
        return Infinity

    def peekType(self):
        try:
            if self.ops[self.index]:
                if iz.number(self.ops[self.index].get('delete')):
                    return 'delete'
                elif iz.number(self.ops[self.index].get('retain')):
                    return 'retain'
                else:
                    return 'insert'
        except:
            pass
        return 'retain'

