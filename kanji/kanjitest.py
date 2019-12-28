import unittest
from kanji_conversion1 import kanji_conversion, kanji

chars = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '百', '千']
kanji_suu = input('漢数字を入力してください')
kanli = list(kanji_suu)
class Testkanji(unittest.TestCase):
    def test_conversion(self):
        inter = set(chars) & set(kanli)
        self.assertEqual(inter, set(kanli))

    def test_notconversion(self):
        exclu = set(chars) ^ set(kanli)
        self.assertNotEqual(exclu, kanli)

if __name__ == '__main__':
    unittest.main()
