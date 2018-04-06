import unittest
from bt_01 import hello


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.i = "Tolik"
        self.hello = "Hello, Tolik!"
        print("Start of the test")

    def tearDown(self):
        print("End of the test\n")

    def test_hello(self):
        """Hello somebody"""
        self.assertEqual(hello(self.i), self.hello)


if __name__ == '__main__':
    unittest.main()
