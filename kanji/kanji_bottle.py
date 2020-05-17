from bottle import run, template, route, request
from kanji_conversion import convert

chars = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '十', '百', '千', '万', '億']

@route('/kanji')
def kanji():
    return template('kanji', text='', in_text='')

@route('/kanji', method='POST')
def do_kanji():
    input_text = request.forms.input_text
    if any(c not in chars for c in input_text):
        print('入力ミス')
        return template('kanji', text='入力ミス', in_text=input_text)
    elif input_text == '':
        print('空の文字列')
        return template('kanji', text='空の文字列',in_text='空の文字列')
    else:
        kanji = convert(input_text)
        return template('kanji', text=kanji, in_text=input_text)

run(host='localhost', port=8080, debug=True)
