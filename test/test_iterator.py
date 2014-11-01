"""@package test_op
@author: Zosia Sobocinska
@date Nov 1, 2014
"""
import unittest
from richtext import op, Delta

INFINITY = float('inf')


class IteratorTest(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.delta = Delta().insert('Hello', {'bold': True}).retain(3).insert(2, {'src': 'http://quilljs.com/'}).delete(4)

    def test_hasNext_true(self):
        iterator = op.iterator(self.delta.ops)
        self.assertTrue(iterator.hasNext())

    def test_hasNext_false(self):
        iterator = op.iterator([])
        self.assertFalse(iterator.hasNext())

    def test_peekLength_offset_eq_0(self):
        iterator = op.iterator(self.delta.ops)
        self.assertEqual(iterator.peekLength(), 5)
        iterator.next()
        self.assertEqual(iterator.peekLength(), 3)
        iterator.next()
        self.assertEqual(iterator.peekLength(), 1)
        iterator.next()
        self.assertEqual(iterator.peekLength(), 4)

    def test_peekLength_offset_gt_0(self):
        iterator = op.iterator(self.delta.ops)
        iterator.next(2)
        self.assertEqual(iterator.peekLength(), 5 - 2)

    def test_peekType(self):
        iterator = op.iterator(self.delta.ops)
        self.assertEqual(iterator.peekType(), 'insert')
        iterator.next()
        self.assertEqual(iterator.peekType(), 'retain')
        iterator.next()
        self.assertEqual(iterator.peekType(), 'insert')
        iterator.next()
        self.assertEqual(iterator.peekType(), 'delete')
        iterator.next()
        self.assertEqual(iterator.peekType(), 'retain')
        iterator.next()

    def test_next(self):
        iterator = op.iterator(self.delta.ops)
        for i in range(len(self.delta.ops)):
            self.assertEqual(iterator.next(), self.delta.ops[i])
        self.assertEqual(iterator.next(), {'retain': INFINITY})
        self.assertEqual(iterator.next(4), {'retain': INFINITY})
        self.assertEqual(iterator.next(), {'retain': INFINITY})

    def test_next_length(self):
        iterator = op.iterator(self.delta.ops)
        self.assertEqual(iterator.next(2), {'insert': 'He', 'attributes': {'bold': True}})
        self.assertEqual(iterator.next(10), {'insert': 'llo', 'attributes': {'bold': True}})
        self.assertEqual(iterator.next(1), {'retain': 1})
        self.assertEqual(iterator.next(2), {'retain': 2})


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
