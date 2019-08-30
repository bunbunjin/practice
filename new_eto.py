class Eto:
    year = 0
    name = ''
    eto_name = ''

    def __init__(self, year, name, eto_name):
        self.year = year
        self.name = name
        self.eto_name = eto_name

    def eto(self):
        print(f'{self.year}生まれ{self.name}さんは{self.eto_name}デス。')


def eto_year():
    year_str = input('あなたの生まれた年を西暦4桁で入力してください')
    year_len = len(year_str)
    year = int(year_str)

    if year > 2020 and year_len != 4:
        print('あああああ')
        quit()

    else:
        return year



def eto():
    eto_tuple = ('子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥',)


    year = eto_year()
    number_of_eto = (year + 8) % 12
    eto_name = eto_tuple[number_of_eto]


    name = input('名前を入力して下さい。')


    e = Eto(year, name, eto_name)
    ana = e.eto()

    return ana


eto()



