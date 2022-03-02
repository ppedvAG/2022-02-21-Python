from unittest import TestCase
import helper


class Test(TestCase):
    def test_subtract(self):
        result = helper.subtract(4, 2)
        self.assertEqual(result, 2)
    def test_add(self):
        result = helper.add(2,2)
        self.assertEqual(result, 4)