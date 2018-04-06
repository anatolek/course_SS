import unittest
from bt_04 import isPalindrome


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.str_true = "radar"
        self.str_false = "radar1"
        print("Start of the test #4")

    def tearDown(self):
        print("End of the test #4\n")

    def test_isPalindromeTrue(self):
        self.assertTrue(isPalindrome(self.str_true))
        print("Testing for a value of 'True'")

    def test_isPalindromeFalse(self):
        self.assertFalse(isPalindrome(self.str_false))
        print("Testing for a value of 'False'")


if __name__ == '__main__':
    unittest.main()
