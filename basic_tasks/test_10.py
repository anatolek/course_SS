import unittest
from bt_10 import charFreq


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.str = "abbabcbdbabdbdbabababcbcbab"
        self.dict = {'a': 7, 'b': 14, 'c': 3, 'd': 3}
        print("Start of the test #10")

    def tearDown(self):
        print("End of the test #10\n")

    def test_charFreq(self):
        self.assertDictEqual(charFreq(self.str), self.dict)


if __name__ == '__main__':
    unittest.main()
