#python3
eto_list = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥',]
#データ追加 "append"
#eto_list.append('猫')
#データ削除 "remove"
#eto_list.remove('丑')
#eto_listの1番目の要素をeto_nameへ代入する
eto_name = eto_list[1]
print('remove()実行前の干支リスト1番は', eto_name, 'です。')
#丑を削除する
eto_list.remove('丑')
#eto_listの1番目の要素をeto_nameへ代入する
eto_name = eto_list[1]
print('remove()実行後の干支リスト1番は', eto_name, 'です。')
#print(eto_list)
