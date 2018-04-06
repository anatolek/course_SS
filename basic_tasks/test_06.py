import unittest
from bt_06 import caesarCipher


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.str = "My name is Anatolii"
        self.key1 = 7
        self.key2 = 90
        self.encoded_str1 = "TF1uhtl1pz1HuhAvspp"
        self.encoded_str2 = "Co[d0c4[8i[qd0jeb88"
        print("Start of the test")

    def tearDown(self):
        print("End of the test\n")

    def test_caesarCipher(self):
        """Create the encoded string"""
        self.assertEqual(caesarCipher(self.str, self.key1), self.encoded_str1)
        self.assertEqual(caesarCipher(self.str, self.key2), self.encoded_str2)


if __name__ == '__main__':
    unittest.main()
