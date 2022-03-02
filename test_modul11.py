import unittest


class test_sum(unittest.TestCase):
    def test_equals(self):
        result = sum((4, 6))
        self.assertEqual(result, 10)

    def test_not_equal(self):
        result = sum((4, 6))
        self.assertNotEqual(result, 25)




