import unittest
from bt_03 import reverse


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.x = "I am testing"
        self.rev_x = "gnitset ma I"

    def tearDown(self):
        print("End of the test\n")

    def test_sum(self):
        """Reverse string"""
        self.assertEqual(reverse(self.x), self.rev_x)


if __name__ == '__main__':
    unittest.main()
