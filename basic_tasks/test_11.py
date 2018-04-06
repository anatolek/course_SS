import unittest
from bt_11 import decToBin


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.dec1 = 174
        self.dec2 = 5671252
        self.bin1 = '01110101'
        self.bin2 = '00101010100100010110101'
        print("Start of the test #11")

    def tearDown(self):
        print("End of the test #11\n")

    def test_decToBin(self):
        self.assertEqual(decToBin(self.dec1), self.bin1)
        self.assertEqual(decToBin(self.dec2), self.bin2)


if __name__ == '__main__':
    unittest.main()
