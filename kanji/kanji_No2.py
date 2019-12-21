kanji = {
    '一' : 1,
    '二' : 2,
    '三' : 3,
    '四' : 4,
    '五' : 5,
    '六' : 6,
    '七' : 7,
    '八' : 8,
    '九' : 9,
    '十' : 10,
    '百' : 100,
    '千' : 1000,
}

def kanji_conversion(kanji_suu):
    kanli = list(kanji_suu)
    answer = [kanji[con] for con in kanli]
    print(answer)
    last = None
    accum = 0
    for digit in answer[:-1]:
        num = 0
        if digit == 1000:
            if last is None:
                num = 1000 * 1
            else:
                num = 1000 * last
                last = None

        elif digit == 100:
            if last is None:
                num = 100 * 1
            else:
                num = 100 * last
                last = None

        elif digit == 10:
            if last == 10:
                num = 10 * 1
            else:
                num = 10 * last
                last = None

        else:
            last = digit

        accum += num
    accum += answer[-1]
    print(accum)


try:
    kanji_conversion(input('漢数字を千の位まで入力してください。'))

except KeyError:
    print('入力にミスがあります。')
