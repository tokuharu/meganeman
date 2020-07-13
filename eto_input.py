# python3
year_str = input('あなたの生まれ年を西暦4桁で入力してください: ')
#入力された値をint型へ変換
year = int(year_str)
# 干支の順番（0~11の範囲）を西暦から計算する
#計算結果を変数に代入
number_of_eto = (year + 8) % 12
#結果を表示
print('あなたの干支の順番は', number_of_eto, '番です。')
