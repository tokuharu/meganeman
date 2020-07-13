#python3
#モジュールをインポート
from datetime import date, datetime

#今日の日付を返す
def today_command():
    today = date.today()
    response = '今日ノ日付ハ {} デス'.format(today)
    return response

#現在日時を返す
def now_command():
    now = datetime.now()
    response = '現在ノ日時ハ {} デス'.format(now)
    return response

#日時を作成
def weekday_command(command):
    try:
        data = command.split()
        year = int(data[1])
        month = int(data[2])
        day = int(data[3])
        one_day = date(year, month, day)

        #曜日の文字列を作成
        weekday_str = '月火水木金土日'
        weekday = weekday_str[one_day.weekday()]

        response = '{} ハ {}曜日デス'.format(one_day, weekday)
    #IndexErrorに対応
    except IndexError:
        response = '3ツノ値(年月日)ヲ指定シテクダサイ'
    #ValueErrorに対応
    except ValueError:
        response = '正シイ日付ヲ指定シテクダサイ'
    return response
