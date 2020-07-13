#python3
#関数を定義
def len_command(command):
    #文字列を取得
    cmd, text = command.split()
    #文字列の長さを取得
    length = len(text)
    #メッセージを返す
    response = '文字列ノ長サハ {} 文字デス。'.format(length)
    return response

def heisei_command(command):
    heisei, year_str = command.split()
    year = int(year_str)
    if year >= 1989:
        heisei_year = year - 1988
        response = '西暦{}年ハ、平成{}年デス。'.format(year, heisei_year)
    else:
        response = '西暦{}年ハ、平成デハアリマセン'.format(year)
    #結果を返す
    return response
#文字コードを指定
command_file = open('pybot.txt', encoding='utf-8')
raw_data = command_file.read()
command_file.close()
#行ごとの文字列に分割
lines = raw_data.splitlines()

#空の辞書を作成
bot_dict = {}
for line in lines:
    #カンマで２つの文字列に分割
    word_list = line.split(',')
    #２つの文字列をキーとバリューとして、辞書にセット
    key = word_list[0]
    response = word_list[1]
    bot_dict[key] = response

while True:
    command = input('pybot> ')
    response = ''
    for key in bot_dict:
        if key in command:
            response = bot_dict[key]
            break
    #『平成』が含まれる場合
    if '平成' in command:
        response = heisei_command(command)
    #長さコマンド追加
    if '長さ' in command:
        response = len_command(command)
        #heisei, year_str = command.split()
        #年を数値に変換
        #year = int(year_str)
        #平成の範囲か？
        #if year >= 1989:
            #平成の年を計算
            #heisei_year = year - 1988
            #response = '西暦{}年ハ、平成{}年デス。'.format(year, heisei_year)
            #平成ではない場合
        #else:
            #response = '西暦{}年ハ、平成デハアリマセン'.format(year)

    if not response:
        response = 'ナニヲイッテルカワカラナイヨ！'
    print(response)

    if 'さようなら' in command:
        break
