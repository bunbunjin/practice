
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
    '万' : 10000,
    '億' : 100000000
}

def convert(kanji_suu):
    answer = [kanji[con] for con in kanji_suu]
    last = None
    accum = 0
    for digit in answer:
        num = 0
        if digit == 100000000:
            if last is None:
                num = 100000000
            else:
                num = 100000000 * last
                last = None

        elif digit == 10000:
            if last is None:
                num = 10000 * 1
            else:
                num = 10000 * last
                last = None

        elif digit == 1000:
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
    return accum