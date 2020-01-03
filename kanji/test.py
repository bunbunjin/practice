import unittest
from kanji_conversion import convert

class Testkanji(unittest.TestCase):
    def test_convert_simple(self):
        self.assertEqual(convert('三百九十七'), 397)

    def test_convert_oku(self):
        self.assertEqual(convert('一億一'), 100000001)

    def test_convert_oku_sen(self):
        self.assertEqual(convert('一億七万五千八百五十四'), 100075854)

if __name__ == '__main__':
    unittest.main()
