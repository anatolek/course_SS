import unittest
from bt_07 import diagonalReverse


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.revMatrix = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
        print("Start of the test #7")

    def tearDown(self):
        print("End of the test #7\n")

    def test_diagonalReverse(self):
        self.assertListEqual(diagonalReverse(self.matrix), self.revMatrix)


if __name__ == '__main__':
    unittest.main()
