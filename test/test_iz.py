"""@package test_iz
@author: Zosia Sobocinska
@date Nov 1, 2014
"""
import unittest
from richtext import iz


class IzEqualTest(unittest.TestCase):

    def test_exact_objects(self):
        obj = {'a': 1, 'b': True, 'c': 'test'}
        self.assertTrue(iz.equal(obj, obj))

    def test_deep_equal_objects(self):
        obj1 = {'a': 1, 'b': True, 'c': 'test'}
        obj2 = {'a': 1, 'c': 'test', 'b': True}
        self.assertTrue(iz.equal(obj1, obj2))

    def test_diffrent_keys(self):
        obj1 = {'a': 1, 'b': True, 'c': 'test'}
        obj2 = {'a': 1, 'c': 'test', 'b': False}
        self.assertFalse(iz.equal(obj1, obj2))

    def test_missing_keys(self):
        obj1 = {'a': 1, 'b': True, 'c': 'test'}
        obj2 = {'a': 1, 'c': 'test'}
        self.assertFalse(iz.equal(obj1, obj2))

    # test_null_and_undefined() has no reason to exist in Python, since Python
    # forces variables being defined

    def test_existing_with_nonexisting(self):
        self.assertFalse(iz.equal({}, None))


class IzArrayTest(unittest.TestCase):

    def test_literal(self):
        self.assertTrue(iz.array([]))

    def test_none(self):
        self.assertFalse(iz.array(None))


class IzNumberTest(unittest.TestCase):

    def test_literal(self):
        self.assertTrue(iz.number(11))

    def test_nan(self):
        self.assertTrue(iz.number(float('NaN')))

    def test_infinity(self):
        self.assertTrue(iz.number(float('inf')))

    def test_none(self):
        self.assertFalse(iz.number(None))

    def test_wrong_type(self):
        self.assertFalse(iz.number({}))


class IzDictionaryTest(unittest.TestCase):

    def test_literal(self):
        self.assertTrue(iz.dictionary({}))

    def test_string_literal(self):
        self.assertFalse(iz.dictionary('test'))

    def test_number_literal(self):
        self.assertFalse(iz.dictionary(1))

    def test_none(self):
        self.assertFalse(iz.dictionary(None))

    def test_object(self):
        self.assertFalse(iz.dictionary(object()))


class IzStringTest(unittest.TestCase):

    def test_str(self):
        self.assertTrue(iz.string('test'))

    def test_unicode(self):
        self.assertTrue(iz.string(u'test'))

    def test_none(self):
        self.assertFalse(iz.string(None))

    def test_wrong_type(self):
        self.assertFalse(iz.string({}))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
