"""@package test_iz
@author: Zosia Sobocinska
@date Nov 1, 2014
"""
import unittest
from richtext import attributes


class AttributesCloneTest(unittest.TestCase):

    attr = {
      'bold': True,
      'color': 'red',
      'italic': None
    }

    def test_undefined(self):
        self.assertEqual(attributes.clone(), {})

    def test_keep_null(self):
        clone = attributes.clone(self.attr, True)
        self.assertFalse(clone is self.attr)
        self.assertEqual(clone, self.attr)

    def test_dont_keep_null(self):
        clone = attributes.clone(self.attr, False)
        self.assertFalse(clone is self.attr)
        self.assertEqual(clone, {
                                 'bold': True,
                                 'color': 'red'
                                 })


class AttributesComposeTest(unittest.TestCase):

    attr = {
      'bold': True,
      'color': 'red',
    }

    def test_left_is_none(self):
        self.assertEqual(attributes.compose(None, self.attr), self.attr)

    def test_right_is_none(self):
        self.assertEqual(attributes.compose(self.attr, None), self.attr)

    def test_both_are_none(self):
        self.assertEqual(attributes.compose(None, None), None)

    def test_missing(self):
        self.assertEqual(attributes.compose(self.attr, {'italic': True}), {
                                                                           'bold': True,
                                                                           'italic': True,
                                                                           'color': 'red',
                                                                           })

    def test_overwrite(self):
        self.assertEqual(attributes.compose(self.attr,
                                            {'bold': False, 'color': 'blue'}
                                            ), {'bold': False, 'color': 'blue'})

    def test_remove(self):
        self.assertEqual(attributes.compose(self.attr, {'bold': None}), {'color': 'red'})

    def test_remove_to_none(self):
        self.assertEqual(attributes.compose(self.attr, {'bold': None, 'color': None}), None)

    def test_remove_missing(self):
        self.assertEqual(attributes.compose(self.attr, {'italic': None}), self.attr)


class AttributesDiffTest(unittest.TestCase):

    format = {'bold': True, 'color': 'red'}

    def test_left_is_none(self):
        self.assertEqual(attributes.diff(None, self.format), self.format)

    def test_right_is_none(self):
        expected = {'bold': None, 'color': None}
        self.assertEqual(attributes.diff(self.format, None), expected)

    def test_same_format(self):
        self.assertEqual(attributes.diff(self.format, self.format), None)

    def test_add_format(self):
        added = {'bold': True, 'italic': True, 'color': 'red'}
        expected = {'italic': True}
        self.assertEqual(attributes.diff(self.format, added), expected)

    def test_remove_format(self):
        removed = {'bold': True}
        expected = {'color': None}
        self.assertEqual(attributes.diff(self.format, removed), expected)

    def test_overwrite_format(self):
        overwritten = {'bold': True, 'color': 'blue'}
        expected = {'color': 'blue'}
        self.assertEqual(attributes.diff(self.format, overwritten), expected)


class AttributesTransformTest(unittest.TestCase):
    left = {'bold': True, 'color': 'red', 'font': None}
    right = {'color': 'blue', 'font': 'serif', 'italic': True}

    def test_left_is_none(self):
        self.assertEqual(attributes.transform(None, self.left, False), self.left)

    def test_right_is_none(self):
        self.assertEqual(attributes.transform(self.left, None, False), None)

    def test_both_are_none(self):
        self.assertEqual(attributes.transform(None, None, False), None)

    def test_with_priority(self):
        expected = {'italic': True}
        self.assertEqual(attributes.transform(self.left, self.right, True), expected)

    def test_without_priority(self):
        self.assertEqual(attributes.transform(self.left, self.right, False), self.right)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
