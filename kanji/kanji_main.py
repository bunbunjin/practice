from kanji_conversion1 import kanji_conversion

kanji_suu = input('漢数字を入力してください')
chars = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '百', '千', '万', '億']

if any(c not in chars for c in kanji_suu):
    raise ValueError('Unknown kanji was input')

else:
    kanji_conversion(kanji_suu)

