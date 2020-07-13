#python3
#辞書データを定義
bot_dict = {
    'こんにちは': 'コンニチハ',
    'ありがとう': 'ドウイタシマシテ',
    'さようなら': 'サヨウナラ',
    }

while True:
    command = input('pybot> ')
    #空文字列で初期化する
    response = ''
    #キーを順番に取り出す
    for message in bot_dict:
        if message in command:
            #対応となる文字列を設定する
            response = bot_dict[message]
            break

    #空文字列の場合
    if not response:
        response = 'ナニヲイッテルカワカラナイヨ！！'
    #対応メッセージを表示
    print(response)

    #whileループを終了
    if 'さようなら' in command:
        break
