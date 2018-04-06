import unittest
from bt_04 import isPalindrome


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.str_true = "radar"
        self.str_false = "radar1"
        print("Start of the test")

    def test_isPalindromeTrue(self):
        self.assertTrue(isPalindrome(self.str_true))

    def test_isPalindromeFalse(self):
        self.assertFalse(isPalindrome(self.str_false))

if __name__ == '__main__':
    unittest.main()
