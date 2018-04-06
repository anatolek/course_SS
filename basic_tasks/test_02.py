import unittest
from bt_02 import _sum, _multiply


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.x = [1, 2, 3, 4]
        self.sum_x = 10
        self.mult_x = 24
        print("Start of the test #2")

    def tearDown(self):
        print("End of the test #2\n")

    def test_sum(self):
        """Sum of two numbers"""
        self.assertEqual(_sum(self.x), self.sum_x)

    def test_multiply(self):
        """Multiplication of two numbers"""
        self.assertEqual(_multiply(self.x), self.mult_x)


if __name__ == '__main__':
    unittest.main()
