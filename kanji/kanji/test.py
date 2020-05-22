import unittest
from conversion import convert

class Testkanji(unittest.TestCase):
    def test_convert_simple(self):
        self.assertEqual(convert('三百九十七'), 397)

    def test_convert_oku(self):
        self.assertEqual(convert('一億一'), 100000001)

    def test_convert_oku_sen(self):
        self.assertEqual(convert('一億七万五千八百五十四'), 100075854)

    def test_convert_sen(self):
        self.assertEqual(convert('四千'), 4000)

    def test_convert_juu(self):
        self.assertEqual(convert('四十'), 40)

    def test_convert_tan(self):
        self.assertEqual(convert('四'), 4)

if __name__ == '__main__':
    unittest.main()
