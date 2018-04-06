import unittest
from bt_02 import _sum, _multiply


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print("Start of the test")

    def tearDown(self):
        print("End of the test\n")

    def test_sum(self):
        """Sum of two numbers"""
        self.assertEqual(_sum([1, 2, 3, 4]), 100)

    def test_multiply(self):
        """Multiplication of two numbers"""
        self.assertEqual(_multiply([1, 2, 3, 4]), 24)


if __name__ == '__main__':
    unittest.main()
