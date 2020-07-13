#python3
#インポートする
from bottle import route, run, template, request
from pybot import pybot

#URLを指定する
@route('/hello')
def hello():
    #テンプレートファイルを指定
    #空文字を渡す
    return template('pybot_template', input_text='', output_text='')

#POSTを追加
@route('/hello', method='POST')
def do_hello():
    #値を取り出す
    input_text = request.forms.input_text
    #pybot()を実行
    output_text = pybot(input_text)
    #値を渡す
    return template('pybot_template', input_text=input_text, output_text=output_text)

#開発サーバーを起動
run(host='localhost', port=8080, debug=True)
