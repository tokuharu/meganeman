#python3
#関数にする
def eto_command(command):
    #年を取得
    eto, year = command.split()
    eto_list = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥",]
    eto_number = (int(year) + 8) % 12
    eto_name = eto_list[eto_number]
    #応答を作成
    response = '{}年生マレノ干支ハ「{}」デス。'.format(year, eto_name)
    return response
