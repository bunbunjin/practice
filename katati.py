import datetime
from pytz import timezone

hiniti = datetime.date.today()

yattakoto = input('今日やったことは何ですか？')
next = input('次やること')
nazo = input('分からなかったこと、困ったこと')
print('\n')
def renraku(yattakoto, next, nazo):
    bun = "{}\nやったこと：{}\n次やること：{}\n困ったこと,分からなかったこと:{}\n"
    kanseibun = bun.format(hiniti, yattakoto, next, nazo)
    open_katati = open('報告会.txt', 'a', encoding = "utf_8")
    open_katati.write('{}'.format(kanseibun))
    open_katati.close()
    print(kanseibun)

renraku(yattakoto, next, nazo)
