import unittest
from bt_09 import close_brackets


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.ok1 = "[]"
        self.ok2 = "[][]"
        self.ok3 = "[[[][[]]]]"
        self.not_ok1 = "]["
        self.not_ok2 = "][]["
        self.not_ok3 = "[]][[]"
        print("Start of the test")

    def tearDown(self):
        print("End of the test\n")

    def test_close_brackets_ok(self):
        self.assertEqual(close_brackets(self.ok1), "OK")
        self.assertEqual(close_brackets(self.ok2), "OK")
        self.assertEqual(close_brackets(self.ok3), "OK")

    def test_close_brackets_ok(self):
        self.assertEqual(close_brackets(self.not_ok1), "NOT OK")
        self.assertEqual(close_brackets(self.not_ok2), "NOT OK")
        self.assertEqual(close_brackets(self.not_ok3), "NOT OK")


if __name__ == '__main__':
    unittest.main()
