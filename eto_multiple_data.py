#python3
#生まれ年を入力
year_str = input('あなたの生まれ年を西暦4桁で入力して下さい: ')
year = int(year_str)
nomuber_of_eto = (year + 8) % 12
#干支のデータのタプルを作成
eto_tupule = ('子',
              '丑',
              '寅',
              '卯',
              '辰',
              '巳',
              '午',
              '未',
              '申',
              '酉',
              '戌',
              '亥',)
#タプルから値を取得して変数へ代入
eto_name = eto_tupule[nomuber_of_eto]
#format()で文字列を生成
print('あなたの干支は{}です。'.format(eto_name))
