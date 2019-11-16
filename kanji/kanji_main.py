#ここにファイル
from kanji_conversion1 import kanji_conversion


kanji_suu = input('漢数字を入力してください')
kanji_jud = kanji_suu.isdigit()



if kanji_jud == False:
    kanji_conversion(kanji_suu)
    #print('ここに結果が出る')


else:
    print('漢数字でお願いします。')