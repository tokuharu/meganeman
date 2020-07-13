#python3
#import文
from pybot_eto import eto_command
from pybot_random import choice_command, dice_command
from pybot_datetime import today_command, now_command, weekday_command
from pybot_weather import weather_command
from pybot_wikipedia import wikipedia_command
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
    #数値に変更可能か確認
    if year_str.isdigit():
        year = int(year_str)
        if year >= 1989:
            heisei_year = year - 1988
            response = '西暦{}年ハ、平成{}年デス。'.format(year, heisei_year)
        else:
            response = '西暦{}年ハ、平成デハアリマセン'.format(year)
    #exceptキーワードをelse文に変更
    else:
        response = '数値ヲ指定シテクダサイ'
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
    response = ""
    #tryキーワード追加
    try:
        for key in bot_dict:
            if key in command:
                response = bot_dict[key]
                break
        #平成コマンド追加
        if '平成' in command:
            response = heisei_command(command)
        #長さコマンド追加
        if '長さ' in command:
            response = len_command(command)
        #干支コマンド追加
        if '干支' in command:
            response = eto_command(command)
        #選ぶコマンド追加
        if '選ぶ' in command:
            response = choice_command(command)
        #さいころコマンド追加
        if 'さいころ' in command:
            response = dice_command()
        #今日の日付コマンド追加
        if '今日' in command:
            response = today_command()
        #現在日時コマンド追加
        if '現在' in command:
            response = now_command()
        #曜日コマンド追加
        if '曜日' in command:
            response = weekday_command(command)
        #天気コマンド追加
        if '天気' in command:
            response = weather_command()
        #事典コマンド追加
        if '事典' in command:
            response = wikipedia_command(command)

        if not response:
            response = 'ナニヲイッテルカワカラナイヨ！'
        print(response)

        if 'さようなら' in command:
            break
    #exceptキーワードを追加
    except Exception as e:
        print('予期セヌ エラーガ 発生シマシタ！！！')
        print('* 種類:', type(e))
        print('* 内容:', e)
