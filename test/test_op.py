"""@package test_op
@author: Zosia Sobocinska
@date Nov 1, 2014
"""
import unittest
from richtext import op


class OpLengthTest(unittest.TestCase):

    def test_delete(self):
        self.assertEqual(op.length({'delete': 5}), 5)

    def test_retain(self):
        self.assertEqual(op.length({'retain': 2}), 2)

    def test_insert_text(self):
        self.assertEqual(op.length({'insert': 'text'}), 4)

    def test_insert_embed(self):
        self.assertEqual(op.length({'insert': 2}), 1)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
